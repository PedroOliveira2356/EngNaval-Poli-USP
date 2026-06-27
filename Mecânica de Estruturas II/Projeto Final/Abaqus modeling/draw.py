"""
Branched line drawer
=====================

For a "main line" between two points it:
  1. places N evenly spaced interior points on it (endpoints excluded),
  2. grows a FIRST branch from every interior point, along the line's normal,
  3. grows a SECOND branch from the tip of the first branch, perpendicular to
     it (i.e. the normal rotated by +/-90 deg).

The second branch shape is set by a type string:
    'T'  -> a bar centred on the tip          (stem + symmetric cross-bar)
    'L1' -> a single arm, normal rotated +90  -> an L
    'L2' -> a single arm, normal rotated -90  -> a mirrored L

Finally the whole drawing is reflected across the y-axis, so a line that
spans x = 0..10 also appears at x = 0..-10 with the same points.

A global LINE_SEGMENTS list holds one (point_a, point_b, N, shape) tuple per
line; the drawing is built by analysing each tuple independently.
"""

import os
import csv
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------- #
#  GLOBAL PARAMETERS FROM INPUT FILE                                          #
# --------------------------------------------------------------------------- #
# Basedir = r"C:\repos\EngNaval-Poli-USP\Mecânica de Estruturas II\Projeto Final\Abaqus modeling"
Basedir = Path(__file__).parent

with open(os.path.join(Basedir, "inputs.csv"), "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    linhas = list(reader)


# Branch lengths can differ per shape. Set them independently here.
#   branch1 = the FIRST branch  (grows from the line, along the normal)
#   branch2 = the SECOND branch (grows from the first branch's tip; per arm)
BRANCH_SIZES = {
    "T": {"branch1": float(linhas[10][1]), "branch2": float(linhas[10][2])},
    "L1": {"branch1": float(linhas[11][1]), "branch2": float(linhas[11][2])},
    "L2": {"branch1": float(linhas[11][1]), "branch2": float(linhas[11][2])},
}


DEFAULT_N = 0  # default number of interior points per line
DEFAULT_SHAPE = "T"  # default second-branch shape: 'T', 'L1', 'L2'

MIRROR_Y = False  # reflect the whole drawing across the y-axis
SHOW_NORMAL = False  # also draw the line's normal as an arrow

# Every drawing is described here. Each element is one INDEPENDENT line:
#     (point_a, point_b, N, shape)
# point_a / point_b : (x, y) endpoints
# N                 : number of interior points (endpoints excluded)
# shape             : 'T', 'L1' or 'L2'
LINE_SEGMENTS = [
    ((0, 0), (10, 0), 4, "T"),
    ((-6, 1), (-1, 8), 3, "L1"),
    ((2, 5), (8, 9), 2, "L2"),
]

# styling
MAIN_COLOR = "#222222"
BRANCH1_COLOR = "#1f77b4"
BRANCH2_COLOR = "#d62728"
NORMAL_COLOR = "#9467bd"
POINT_COLOR = "#2ca02c"
MIRROR_ALPHA = 0.40  # transparency of the mirrored twin
MAIN_WIDTH = 1.0
BRANCH_WIDTH = 1.0
POINT_SIZE = 10
FIG_SIZE = (9, 9)


# --------------------------------------------------------------------------- #
#  VECTOR HELPERS                                                             #
# --------------------------------------------------------------------------- #
def _arr(p):
    """Coerce a point/vector to a float numpy array."""
    return np.asarray(p, dtype=float)


def unit(v):
    """Return the unit vector of v."""
    v = _arr(v)
    n = np.hypot(v[0], v[1])
    if n == 0:
        raise ValueError("Cannot normalise a zero-length vector.")
    return v / n


def rotate(v, deg):
    """Rotate a 2-D vector by `deg` degrees (counter-clockwise)."""
    r = np.deg2rad(deg)
    c, s = np.cos(r), np.sin(r)
    v = _arr(v)
    return np.array([c * v[0] - s * v[1], s * v[0] + c * v[1]])


def line_normal(a, b):
    """Unit normal of segment a->b, i.e. direction (-dy, dx)."""
    a, b = _arr(a), _arr(b)
    d = b - a
    return unit(np.array([-d[1], d[0]]))


def branch_lengths(shape):
    """Return (branch1_length, branch2_length) for a shape, validated."""
    shape = shape.upper()
    if shape not in BRANCH_SIZES:
        raise ValueError(f"Unknown shape '{shape}'. Use one of {list(BRANCH_SIZES)}.")
    s = BRANCH_SIZES[shape]
    return s["branch1"], s["branch2"]


def interior_points(a, b, n):
    """N points evenly spread on a->b, with both endpoints excluded."""
    a, b = _arr(a), _arr(b)
    fracs = np.arange(1, n + 1) / (n + 1)  # i/(n+1) for i = 1..n
    return [a + f * (b - a) for f in fracs]


# --------------------------------------------------------------------------- #
#  BRANCH CONSTRUCTION                                                        #
# --------------------------------------------------------------------------- #
# A segment is a dict: {"p1": ndarray, "p2": ndarray, "kind": str}


def build_branches(point, normal, shape):
    """
    Build the first + second branch segments growing from one interior `point`.
    `normal` is the (unit) direction of the first branch.
    """
    shape = shape.upper()
    point = _arr(point)
    l1, l2 = branch_lengths(shape)

    # first branch: from the point, along the normal
    tip = point + l1 * normal
    segs = [{"p1": point, "p2": tip, "kind": "branch1"}]

    # second branch is perpendicular to the first == normal rotated +/-90 deg
    perp_plus = rotate(normal, +90)  # 'L1' direction
    perp_minus = rotate(normal, -90)  # 'L2' direction

    if shape == "T":
        segs.append(
            {
                "p1": tip + l2 * perp_minus / 2,
                "p2": tip + l2 * perp_plus / 2,
                "kind": "branch2",
            }
        )
    elif shape == "L1":
        segs.append({"p1": tip, "p2": tip + l2 * perp_plus, "kind": "branch2"})
    elif shape == "L2":
        segs.append({"p1": tip, "p2": tip + l2 * perp_minus, "kind": "branch2"})

    return segs


def build_line_segments(a, b, n, shape):
    """
    Build every segment for ONE main line a->b: the main line plus the
    first + second branches at each of the N interior points.

    Returns (segments, points, normal).
    """
    a, b = _arr(a), _arr(b)
    normal = line_normal(a, b)
    pts = interior_points(a, b, n)

    segments = [{"p1": a, "p2": b, "kind": "main"}]
    if SHOW_NORMAL:
        l1, _ = branch_lengths(shape)
        mid = 0.5 * (a + b)
        segments.append({"p1": mid, "p2": mid + l1 * normal, "kind": "normal"})

    for p in pts:
        segments.extend(build_branches(p, normal, shape))

    return segments, pts, normal


def mirror_segments(segments):
    """Reflect a list of segments across the y-axis (x -> -x)."""
    flip = np.array([-1.0, 1.0])
    return [
        {"p1": s["p1"] * flip, "p2": s["p2"] * flip, "kind": s["kind"]}
        for s in segments
    ]


# --------------------------------------------------------------------------- #
#  PLOTTING                                                                   #
# --------------------------------------------------------------------------- #
_KIND_STYLE = {
    "main": (MAIN_COLOR, MAIN_WIDTH),
    "branch1": (BRANCH1_COLOR, BRANCH_WIDTH),
    "branch2": (BRANCH2_COLOR, BRANCH_WIDTH),
    "normal": (NORMAL_COLOR, 1.0),
}


def plot_segments(ax, segments, points=None, alpha=1.0):
    """Draw a list of segments (and optional point markers) on `ax`."""
    for s in segments:
        color, width = _KIND_STYLE[s["kind"]]
        (x1, y1), (x2, y2) = s["p1"], s["p2"]
        ax.plot(
            [x1, x2],
            [y1, y2],
            color=color,
            lw=width,
            alpha=alpha,
            solid_capstyle="round",
        )
    if points:
        xs = [p[0] for p in points]
        ys = [p[1] for p in points]
        ax.scatter(xs, ys, s=POINT_SIZE, color=POINT_COLOR, alpha=alpha, zorder=3)


def _finish_axis(ax):
    ax.set_aspect("equal", adjustable="datalim")
    ax.axis('off')  # Remove all axes
    # ax.grid(True, ls=":", alpha=0.4)
    # ax.axhline(0, color="grey", lw=0.6)
    # ax.axvline(0, color="grey", lw=0.6)
    ax.set_title("Midship sketch")


# --------------------------------------------------------------------------- #
#  PUBLIC API                                                                 #
# --------------------------------------------------------------------------- #
def draw_shape(a, b, n=DEFAULT_N, shape=DEFAULT_SHAPE, ax=None):
    """
    Draw ONE branched line from point `a` to point `b`.

    a, b   : (x, y) points in the cartesian plane
    n      : number of interior points (endpoints are never included)
    shape  : 'T', 'L1' or 'L2' (second-branch shape)
    ax     : optional existing axis to draw on (used when chaining lines)

    Returns (points, normal):
        points : list of the N interior coordinates (each an ndarray)
        normal : unit normal of the line (ndarray)
    """
    own_axis = ax is None
    if own_axis:
        _, ax = plt.subplots(figsize=FIG_SIZE)

    segments, points, normal = build_line_segments(a, b, n, shape)
    plot_segments(ax, segments, points, alpha=1.0)

    if MIRROR_Y:
        flip = np.array([-1.0, 1.0])
        plot_segments(
            ax,
            mirror_segments(segments),
            [p * flip for p in points],
            alpha=MIRROR_ALPHA,
        )

    if own_axis:
        _finish_axis(ax)
        plt.show()

    return points, normal


def branch_extreme_points(segments, mirror=False, group=False):
    """
    Collect the extreme (end) points of every first and second branch.

    `segments` is the same list passed to draw_segments(): each element is a
    (point_a, point_b, N, shape) tuple.

    For every interior point a line produces, there are 4 extreme points,
    returned in this fixed order:
        0 : first  branch foot  (the point sitting on the main line)
        1 : first  branch tip
        2 : second branch end A
        3 : second branch end B
    So each segment contributes 4 * N points (N = its interior-point count).
    Note: for 'L1'/'L2' the second branch starts at the first branch tip, so
    points 1 and 2 coincide for those shapes.

    Parameters
    ----------
    mirror : if True, also append each point's y-axis reflection (x -> -x),
             matching the mirrored twin in the plot (doubles the count).
    group  : if True, return one list per segment instead of one flat list.

    Returns
    -------
    A flat list of (x, y) tuples (or, with group=True, a list of such lists).
    """
    flip = np.array([-1.0, 1.0])
    all_groups = []

    for a, b, n, shape in segments:
        normal = line_normal(a, b)
        seg_pts = []
        for p in interior_points(a, b, n):
            b1, b2 = build_branches(p, normal, shape)
            for seg in (b1, b2):
                for end in ("p1", "p2"):
                    pt = seg[end]
                    seg_pts.append((float(pt[0]), float(pt[1])))
                    if mirror:
                        m = pt * flip
                        seg_pts.append((float(m[0]), float(m[1])))
        all_groups.append(seg_pts)

    if group:
        return all_groups

    aux_list = [pt for grp in all_groups for pt in grp]

    # make segments with consecutive points, elem 0 and 1, 2 and 3, etc
    segments = []
    for i in range(0, len(aux_list) - 1, 2):
        segments.append((aux_list[i], aux_list[i + 1]))
    return segments


def draw_segments(segments=None):
    """
    Draw every line described in `segments` (defaults to the global
    LINE_SEGMENTS), each one INDEPENDENTLY, all on a single figure.

    Each element is a 4-tuple: (point_a, point_b, N, shape).
    Returns the list of (points, normal) results, one per line.
    """
    if segments is None:
        segments = LINE_SEGMENTS

    _, ax = plt.subplots(figsize=FIG_SIZE)

    results = []
    for a, b, n, shape in segments:
        results.append(draw_shape(a, b, n=n, shape=shape, ax=ax))

    _finish_axis(ax)
    plt.show()
