import numpy as np
import math
np.set_printoptions(precision=4, suppress=True)

def decLU(t,dp,ds,di):   # (t: Any, dp: Any, ds: Any, di: Any) -> tuple[NDArray[float64], NDArray[float64]]
    '''
    Funcao que recebe a matriz tridiagonal A vetorizada entre:
     -> t  = tamanho da matriz
     -> dp = diag. principal
     -> ds = diag. secundaria superior
     -> di = diag. secundaria inferior
    e devolve as matrizes L e U da decomposicao LU de A.
    '''

    u = np.zeros(t)
    l = np.zeros(t-1)
    u[0] = dp[0]
    for i in range(1,t):
        l[i-1] = di[i]/u[i-1]
        u[i] = dp[i] - l[i-1]*ds[i-1]
    return u,l

def resolutor(t,p,q,ds,r):   # (t: Any, p: Any, q: Any, ds: Any, r: Any) -> NDArray[float64]
    '''
    Funcao que encontra a solucao do sistema Ax = d, tomando como parametros:
     -> t  = tamanho da matriz
     -> p  = vetor da matriz L da decomposicao LU de A
     -> q  = vetor da matriz U da decomposicao LU de A
     -> ds = diag. secundaria superior da matriz A
     -> r  = vetor representando d
     e devolve o vetor x, solucao do sistema.
    '''

    # Passo inicial: encontrar y tal que Ly = d
    y = np.zeros(t)
    y[0] = r[0]
    for i in range(1,t):
        y[i] = r[i] - p[i-1]*y[i-1]

    # Passo final: encontrar x tal que Ux = y
    x = np.zeros(t)
    x[-1] = y[-1]/q[-1]
    for j in range(t-2,-1,-1):
        x[j] = (y[j] - ds[j]*x[j+1])/q[j]

    # Retorna o vetor solucao, x
    return x

def tridi(t,dp,ds,di,r):   # (t: Any, d: Any, e: Any, f: Any, r: Any) -> NDArray
    '''
    Funcao que prepara uma matriz tridiagonal ciclica A e executa
    a solucao do sistema Ax = d para este caso, segundo os parametros:
     -> t = tamanho da matriz
     -> dp = diag. principal
     -> ds = diag. secundaria superior
     -> di = diag. secundaria inferior
     -> r  = vetor representando d
    e devolve o vetor x, solucao do sistema.

    Esta funcao se utiliza das funcoes decLU e resolutor, definidas acima.
    '''

    v = np.zeros(t-1)
    v[0] = di[0]; v[-1] = ds[-2]
    w = np.zeros(t-1)
    w[0] = ds[-1]; w[-1] = di[-1]
    u_barra, l_barra = decLU(t-1,dp[:-1],ds[:-1],di[:-1])

    # Os sistemas descritos abaixo sao eluciados do enunciado do EP
    # T é a submatriz tridiagonal principal (N-1xN-1), obtida da matriz A
    
    # Calculo da solucao do sistema T*y_barra = d_barra
    y_barra = resolutor(t-1,l_barra,u_barra,ds[:-1],r[:-1])

    # Calculo da solucao do sistema T*x_barra = v
    z_barra = resolutor(t-1,l_barra,u_barra,ds[:-1],v)

    x_n = (r[-1] - ds[-1]*y_barra[0] - di[-1]*y_barra[-1])/(
                dp[-1] - ds[-1]*z_barra[0] - di[-1]*z_barra[-1]
    )
    x_barra = y_barra - x_n*z_barra

    return np.append(x_barra, x_n)

def main():   # () -> None
    '''
    A funcao principal do problema, onde sao explicitados os
    parametros determinantes para a funcionalidade das outras
    funcoes do EP e sao impressos os resultados do sistema Ax = d.

    Pede-se para o usuario digitar o tamanho da matriz e informar
    se ela é uma matriz tridiagonal simples ou ciclica. Para a
    matriz simples, pede-se ao usuario se ele deseja visualizar
    as matrizes vetorizadas L e U da decomposicao LU de A.
    '''
    n = int(input('Digite o tamanho da matriz (NxN): '))
    a = np.ones(n)
    b = np.ones(n)*2
    c = np.ones(n)
    d = np.ones(n)
    for i in range(1,n):
        a[i-1] = (2*i - 1)/(4*i)
    a[-1] = (2*n-1)/(2*n)
    for i in range(n):
        c[i] = 1 - a[i]
        d[i] = math.cos((2*math.pi*(i+1)**2)/(n**2))

    tri = bool(int(input('Matriz tridiagonal ciclica? [1:SIM // 0:NAO] ')))
    if tri:
        X = tridi(n,b,c,a,d)
    else:
        U, L = decLU(n,b,c,a)
        X = resolutor(n,L,U,c,d)

    # Etapa destinada a impressao de resultados
    print()
    print(f' --- Vetores utilizados para n = {n} ---')
    print('a =', a)
    print('b =', b)
    print('c =', c)
    print('d =', d)
    if not tri:
        if bool(int(input('Observar os vetores da decomposicao LU? [1:SIM // 0:NAO] '))):
            print()
            print(' --- Decomposicao LU da matriz A ---')
            print('L = ', L)
            print('U = ', U)
    print()
    print(' --- Vetor solucao de Ax = d --- ')
    print('x = ', X)

main()