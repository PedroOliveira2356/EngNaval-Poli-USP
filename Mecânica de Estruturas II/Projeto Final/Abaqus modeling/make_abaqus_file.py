import os
import csv
from pathlib import Path

from draw import *

# Basedir = r"C:\repos\EngNaval-Poli-USP\Mecânica de Estruturas II\Projeto Final\Abaqus modeling"
Basedir = Path(__file__).parent

# Read inputs csv file
with open(os.path.join(Basedir, "inputs.csv"), "r", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    linhas = list(reader)

R_canto = float(linhas[0][1])
H_fundo = float(linhas[1][1])
H1 = float(linhas[2][1])
H2 = float(linhas[3][1])
H3 = float(linhas[4][1])
H4 = float(linhas[5][1])
B1 = float(linhas[6][1])
B2 = float(linhas[7][1])
B_cost = float(linhas[8][1])
Comprimento_SM = float(linhas[9][1])
# Ref_T = [float(linhas[10][1]), float(linhas[10][2])]
# Ref_L = [float(linhas[11][1]), float(linhas[11][2])]

N_ref = [int(linhas[13][1]),
         int(linhas[14][1]),
         int(linhas[15][1]),
         int(linhas[16][1]),
         int(linhas[17][1]),
         int(linhas[18][1]),
         int(linhas[19][1]),
         int(linhas[20][1]),
         int(linhas[21][1]),
         int(linhas[22][1]),
         int(linhas[23][1]),
         int(linhas[24][1]),
         int(linhas[25][1]),]

# utils
Ht = R_canto + H1 + H2 + H3 + H4
Bt = R_canto + B1 + B2

# Condicoes ambientais
g = 9.81
rho_mar = 1025.0
# calado = 7.5

# Material properties
material_name = "Steel"
young_mod_st = float(206e9)
poiss = 0.3
density_st = 7800.0

# Mesh parameters
mesh_size = 0.3


# Point mapping
points = [
    (0.0, 0.0),  # 0
    (0.0, H_fundo),  # 1
    (0.0, Ht),  # 2
    (B1, 0.0),  # 3
    (B1 + B2, 0.0),  # 4
    (B1, H_fundo),  # 5
    (Bt, R_canto),  # 6
    (Bt - B_cost, R_canto + H1),  # 7
    (Bt, R_canto + H1),  # 8
    (Bt - B_cost, R_canto + H1 + H2),  # 9
    (Bt, R_canto + H1 + H2),  # 10
    (Bt - B_cost, R_canto + H1 + H2 + H4),  # 11
    (Bt, R_canto + H1 + H2 + H4),  # 12
    (Bt - B_cost, Ht),  # 13
    (Bt, Ht),  # 14
]

# Define segments with their respective thickness and type
composed_segments = [
    # Central
    (points[0], points[1], 0, "T"),
    (points[1], points[2], N_ref[0], "L1"),
    # Fundo
    (points[0], points[3], N_ref[1], "T"),
    (points[5], points[1], N_ref[2], "T"),
    (points[3], points[5], 0, "L2"),
    # Superior
    (points[13], points[2], N_ref[3], "T"),
    # Canto
    (points[7], points[5], N_ref[4], "L2"),
    (points[3], points[4], N_ref[5], "T"),
    (points[6], points[8], N_ref[6], "L1"),
    (points[7], points[8], 0, "T"),
    # Laterais - verticais
    (points[8], points[10], N_ref[7], "L1"),
    (points[10], points[12], N_ref[8], "L1"),
    (points[12], points[14], N_ref[9], "L1"),
    (points[9], points[7], N_ref[10], "L2"),
    (points[11], points[9], N_ref[11], "L2"),
    (points[13], points[11], N_ref[12], "L2"),
    # Laterais - horizontais
    (points[9], points[10], 0, "L1"),
    (points[11], points[12], 0, "L1"),
    (points[13], points[14], 0, "L1"),
]

mirror_segments = []
for seg in composed_segments:
    if not (seg[0][0] == 0.0 and seg[1][0] == 0.0):
        sh = "T"
        if seg[3] == "L1":
            sh = "L2"
        elif seg[3] == "L2":
            sh = "L1"
        mirror_segments.append(
            ((-seg[1][0], seg[1][1]), (-seg[0][0], seg[0][1]), seg[2], sh)
        )
composed_segments.extend(mirror_segments)

pure_segments = [elem[0:2] for elem in composed_segments]
ref_segments = branch_extreme_points(composed_segments)
total_segments = pure_segments + ref_segments


def make_file():
    model_param = """from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *

# Create new model
Mdb()
MyModel = mdb.models["Model-1"]
"""

    # Create part
    part_name = "midship"

    model_param += f"""\n\ndef create_sketch():
    # Create new part: conves
    MyModel.ConstrainedSketch(name='__profile__', sheetSize=200.0)\n\n"""

    for elem in total_segments:
        model_param += f"""    MyModel.sketches['__profile__'].Line(point1=({elem[0][0]}, {elem[0][1]}), point2=({elem[1][0]}, {elem[1][1]}))\n"""

    model_param += f"""\n    MyModel.sketches['__profile__'].ArcByCenterEnds(center=({Bt-R_canto}, {R_canto}), direction=COUNTERCLOCKWISE, point1=({B1+B2}, {0.0}), point2=({Bt}, {R_canto}))\n"""
    model_param += f"""    MyModel.sketches['__profile__'].ArcByCenterEnds(center=({-(Bt-R_canto)}, {R_canto}), direction=CLOCKWISE, point1=({-(B1+B2)}, {0.0}), point2=({-Bt}, {R_canto}))\n\n"""

    model_param += f"""    MyModel.Part(dimensionality=THREE_D, name='midship', type=DEFORMABLE_BODY)
    MyModel.parts['midship'].BaseShellExtrude(depth={Comprimento_SM}, sketch=
        MyModel.sketches['__profile__'])
    del MyModel.sketches['__profile__']
    """

    # Create material
    model_param += f"""\n\ndef material():
    MyModel.Material(name='{material_name}')
    MyModel.materials['{material_name}'].Elastic(table=(({young_mod_st}, {poiss}), ))
    MyModel.materials['{material_name}'].Density(table=(({density_st}, ), ))
"""

    # Create section and assignments
    model_param += f"""\n\ndef section():
    pass
"""

    # Create assembly
    model_param += f"""\n\ndef assembly():
    MyModel.rootAssembly.DatumCsysByDefault(CARTESIAN)

    MyModel.rootAssembly.Instance(dependent=ON,
        name='{part_name}-1', part=MyModel.parts['{part_name}'])
"""

    # Create step
    model_param += """\n\ndef step():
    MyModel.StaticStep(initialInc=0.01, maxInc=0.01, name='Step-1',
        nlgeom=OFF, previous='Initial')
    MyModel.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'U', 'RF'))
"""

    # Create interactions
    model_param += f"""\n\ndef interaction():
    pass
"""

    # Create loads
    model_param += f"""\n\ndef loads():
    pass
"""

    # creates the mesh
    model_param += f"""\n\ndef mesh():
    MyModel.parts['{part_name}'].seedPart(deviationFactor=0.1,
        minSizeFactor=0.1, size={mesh_size})
    MyModel.parts['{part_name}'].generateMesh()
"""

    # Creates the job
    model_param += """\n\ndef job():
    mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF,
        explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF,
        memory=90, memoryUnits=PERCENTAGE, model='Model-1', modelPrint=OFF,
        multiprocessingMode=DEFAULT, name='Job-1', nodalOutputPrecision=SINGLE,
        numCpus=1, numGPUs=0, queue=None, resultsFormat=ODB, scratch='', type=
        ANALYSIS, userSubroutine='', waitHours=0, waitMinutes=0)

    mdb.jobs['Job-1'].submit(consistencyChecking=OFF)
    mdb.jobs['Job-1'].waitForCompletion()
"""

    # functions call
    model_param += """\n\ncreate_sketch()
material()
section()
assembly()
step()
interaction()
loads()
mesh()
# job()
"""

    # Write the model parameters to a Python file
    with open(os.path.join(Basedir, "Model.py"), "w", encoding="utf-8") as f:
        f.write(model_param)


# draw_segments(composed_segments)
make_file()
