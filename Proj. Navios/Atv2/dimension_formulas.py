import math


def Fn(vel_servico, lenght_bp):
    return vel_servico / math.sqrt(9.81 * lenght_bp)


def vol_desl(coef_bloco, lenght_bp, breadth, draft):
    # volume deslocado em m3
    return coef_bloco * lenght_bp * breadth * draft * 1.005


def desl(coef_bloco, lenght_bp, breadth, draft):
    # deslocamento em ton
    return 1.025 * vol_desl(coef_bloco, lenght_bp, breadth, draft)


def C_alm(coef_bloco, lenght_bp, breadth, draft, pot, vel_servico):
    # Coef de almirantado
    desloc = desl(coef_bloco, lenght_bp, breadth, draft)
    return desloc ** (2 / 3) * vel_servico**3 / pot


def C_b_Wat(froude_num):
    # Coef de bloco - Watson e Gilfillan
    return 0.7 + math.atan((23 - 100 * froude_num) / 4) / 8


def C_DWT(dwt, desloc):
    # Coef de porte bruto
    return dwt / desloc


def W_PL(dwt, desloc):
    # Peso líquido do navio
    return desloc / (1 + C_DWT(dwt, desloc))


def C_b_Jap(froude_num):
    # Coef de bloco - Japão; 0.15 <= Fn <= 0.32
    return (
        -4.22 + 27.81 * math.sqrt(froude_num) - 39.1 * froude_num + 46.6 * froude_num**3
    )


def C_m(coef_bloco):
    # Coef de seção mestra
    return 1 / (1 + (1 - coef_bloco) ** 3.5)


def C_P(
    desloc=None,
    area_secao_mestra=None,
    lenght_bp=None,
    coef_bloco=None,
    coef_secao_mestra=None,
):
    # Coef prismatico long
    if desloc is not None and area_secao_mestra is not None and lenght_bp is not None:
        return desloc / (area_secao_mestra * lenght_bp)
    elif coef_bloco is not None and coef_secao_mestra is not None:
        return coef_bloco / coef_secao_mestra
    else:
        raise ValueError(
            "Provide either (desloc, area_secao_mestra, lenght_bp) or (coef_bloco, coef_secao_mestra)"
        )


def C_PV(vol_desloc, area_linha_dagua, draft):
    # Coef prismatico vertical
    return vol_desloc / (area_linha_dagua * draft)


def C_WL(coef_bloco):
    # Coef de area de linha dagua
    return coef_bloco / (0.471 + 0.551 * coef_bloco)


def A_WL(coef_linha_dagua, lenght_bp, breadth):
    # Area de linha dagua
    return coef_linha_dagua * lenght_bp * breadth


def KB(draft, coef_prismatico_vertical):
    # Altura do centro de carena
    return draft * (2.5 - coef_prismatico_vertical) / 3


def C_I(coef_linha_dagua):
    # Coef de inercia transversal do plano de linha dagua
    return 0.0727 * coef_linha_dagua**2 + 0.0106 * coef_linha_dagua - 0.003


def C_IL(coef_linha_dagua):
    # Coef de inercia longitudinal do plano de linha dagua
    return 0.35 * coef_linha_dagua**2 - 0.405 * coef_linha_dagua + 0.146


def BM_T(
    coef_inercia_transversal, coef_inercia_longitudinal, lenght_bp, breadth, desloc
):
    # Metacentro transversal e longitudinal
    return (
        coef_inercia_transversal * lenght_bp * breadth**3 / desloc,
        coef_inercia_longitudinal * lenght_bp**3 * breadth / desloc,
    )


def KG(depth):
    # Altura do centro de gravidade
    return 0.69 * depth


def GM(kb, bm, kg):
    # Metacentro transversal ou longitudinal
    return kb + bm - 1.03 * kg


def LCB(coef_prismatico_transversal):
    # Longitudinal center of buoyancy
    return -13.5 + 19.4 * coef_prismatico_transversal
