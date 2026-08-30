import math


def deslocamento(c_b, l, b, draft):
    return 1.025 * 1.005 * c_b * l * b * draft


def C_b_Wat(fn):
    # Coef de bloco - Watson e Gilfillan
    return 0.7 + math.atan((23 - 100 * fn) / 4) / 8


def C_b_Jap(fn):
    # Coef de bloco - Japão; 0.15 <= Fn <= 0.32
    return -4.22 + 27.81 * math.sqrt(fn) - 39.1 * fn + 46.6 * fn**3


def C_m(c_b):
    # Coef de seção mestra
    return 1 / (1 + (1 - c_b) ** 3.5)


def C_P(desloc=None, a_sm=None, l=None, c_b=None, c_m=None):
    # Coef prismatico long
    if desloc is not None and a_sm is not None and l is not None:
        return desloc / (a_sm * l)
    elif c_b is not None and c_m is not None:
        return c_b / c_m
    else:
        raise ValueError("Provide either (desloc, a_sm, l) or (c_b, c_m)")


def C_PV(v, a_wl, d):
    # Coef prismatico vertical
    return v / (a_wl * d)


def C_WL(c_b):
    # Coef de area de linha dagua
    return c_b / (0.471 + 0.551 * c_b)


def A_WL(c_wl, l, b):
    # Area de linha dagua
    return c_wl * l * b


def KB(d, c_pv):
    # Altura do centro de carena
    return d * (2.5 - c_pv) / 3


def C_I(c_wl):
    # Coef de inercia transversal do plano de linha dagua
    return 0.0727 * c_wl**2 + 0.0106 * c_wl - 0.003


def C_IL(c_wl):
    # Coef de inercia longitudinal do plano de linha dagua
    return 0.35 * c_wl**2 - 0.405 * c_wl + 0.146


def KG(depth):
    return 0.69 * depth


def GM(kb, bm, kg):
    return kb + bm - kg


def LCB(c_p):
    return -13.5 + 19.4*c_p
