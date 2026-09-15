# Comprimento entre perpendiculares
def LBP_dwt(dwt):
    return 75.72 + 0.003763 * dwt - 2.987e-08 * dwt**2 + 8.613e-14 * dwt**3


def LBP_dwt_vs(dwt, vel_servico):
    return (
        -8.03328214913538e-9 * dwt**2
        + 0.0022750999603707 * dwt
        + 11.778462148958 * vel_servico
        + 6.26122985125173
    )


def LBP_TUD(dwt):
    return 41.647 * dwt**0.133


# Boca
def B_dwt(dwt):
    return 9.031 + 0.1036 * dwt ** (1 / 2)


def B_lbp(lenght_bp):
    return -0.6694 + 0.1762 * lenght_bp


def B_TUD(dwt):
    return min(15.04 + 0.000369 * dwt, 32.2)


# Pontal
def D_dwt(dwt):
    return 5.63 + 0.0004612 * dwt - 4.425e-09 * dwt**2 + 1.416e-14 * dwt**3


def D_b(breadth):
    return 0.114 + 0.5189 * breadth


def D_TUD(dwt):
    return 9.69 + 0.000188 * dwt


# Calado
def d_dwt(dwt):
    return 5.091 + 0.0002359 * dwt - 2.259e-09 * dwt**2 + 7.891e-15 * dwt**3


def d_TUD(dwt):
    return 7.41 + 0.000106 * dwt


# Froud
def Fn_dwt(dwt):
    return 0.2353 - 0.0002292 * dwt ** (1 / 2)
