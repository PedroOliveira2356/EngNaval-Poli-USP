# Comprimento entre perpendiculares
def LBP_dwt(dwt):
    return 77.98 + 0.00301 * dwt - 1.598e-08 * dwt**2 + 2.876e-14 * dwt**3


def LBP_dwt_vs(dwt, vs):
    return (
        -3.16425861316327e-9 * dwt**2
        + 0.00163086454595442 * dwt
        + 17.1400809131358 * vs
        - 25.7937290885904
    )


def LBP_TUD(dwt):
    return 41.647 * dwt**0.133


# Boca
def B_dwt(dwt):
    return 14.9 + 0.0003423 * dwt - 6.641e-10 * dwt**2


def B_lbp(lbp):
    return -1.301 + 0.1825 * lbp


def B_TUD(dwt):
    return min(15.04 + 0.000369 * dwt, 32.2)


# Pontal
def D_dwt(dwt):
    return (
        5.39
        + 0.0004656 * dwt
        - 4.659e-09 * dwt**2
        + 1.957e-14 * dwt**3
        - 2.762e-20 * dwt**4
    )


def D_b(b):
    return 0.114 + 0.5189 * b


def D_TUD(dwt):
    return 9.69 + 0.000188 * dwt


# Calado
def d_dwt(dwt):
    return 5.319 + 0.0001673 * dwt - 8.836e-10 * dwt**2 + 1.686e-15 * dwt**3


def d_TUD(dwt):
    return 7.41 + 0.000106 * dwt
