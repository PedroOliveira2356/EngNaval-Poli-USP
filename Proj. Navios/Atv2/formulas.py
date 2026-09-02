import math


def Fn(vs, l):
    return vs / math.sqrt(9.81 * l)


def vol_desl(c_b, l, b, draft):
    # volume deslocado em m3
    return c_b * l * b * draft * 1.005


def desl(c_b, l, b, draft):
    # deslocamento em ton
    return 1.025 * vol_desl(c_b, l, b, draft)


def C_alm(c_b, l, b, draft, pot, vs):
    # Coef de almirantado
    return desl(c_b, l, b, draft)**(2/3) * vs**3 / pot


def C_b_Wat(fn):
    # Coef de bloco - Watson e Gilfillan
    return 0.7 + math.atan((23 - 100 * fn) / 4) / 8


def C_DWT(dwt, desloc):
    # Coef de porte bruto
    return dwt / desloc


def W_PL(dwt, desloc):
    # Peso líquido do navio
    return desloc / (1 + C_DWT(dwt, desloc))


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


def BM_T(c_i, c_il, l, b, desloc):
    # Metacentro transversal e longitudinal
    return (c_i * l * b**3 / desloc, c_il * l**3 * b / desloc)


def KG(depth):
    return 0.69 * depth


def GM(kb, bm, kg):
    return kb + bm - 1.03 * kg


def LCB(c_p):
    return -13.5 + 19.4 * c_p


def estimar_potencia_tanker(l, b, d, cb, vs):
    """
    Estima a potência necessária do motor (Brake Power) de um navio petroleiro 
    usando o método simplificado da Superfície Molhada (Denny-Mumford).

    Parâmetros:
    l (float): Comprimento do navio (metros)
    b (float): Boca do navio (metros)
    d (float): Calado do navio (metros)
    cb (float): Coeficiente de bloco
    vs (float): Velocidade de serviço (nós)

    Retorna:
    float: A potência efetiva do motor (kW).
    """

    # 1. Constantes estatísticas assumidas para petroleiros
    rho = 1025.0       # Densidade da água do mar (kg/m³)
    Ct = 0.0030        # Coeficiente de resistência total

    # 3. Cálculo da Superfície Molhada (S) - Fórmula de Denny-Mumford
    S = l * (cb * b + 1.7 * d)

    # 4. Cálculo da Resistência Total (Rt) em Newtons
    Rt = 0.5 * rho * Ct * S * (vs ** 2)

    return (Rt * vs) / 1000.0