import numpy as np
np.set_printoptions(precision=4, suppress=True)

def func(L, x):
    '''
    Funcao que retorna o valor de um polinomio descrito atraves de uma lista/array num ponto x
    --> L = lista polinomial (1D)
    --> x = variavel
    '''
    S = 0
    for exp in range(len(L)):
        S += L[exp]*x**exp
    return S

def integr(L, a, b):
    '''
    Funcao que integra polinomio descrito atraves de uma lista/array. Retorna o valor da integral
    --> L   = lista polinomial (1D)
    --> a   = intervalo inferior
    --> b   = intervalo superior
    
    '''
    I = 0
    for exp in range(len(L)):
        I += L[exp]/(exp+1)*(b**(exp+1)-a**(exp+1))
    return I

def cria_matriz(k, xizes, f_resp):
    '''
    Funcao que gera os elementos funcamentais do sistema linear Ax = d, onde A = matriz tridiagonal formada pelos produtos internos dos phi_i e d = vetor coluna formado pelos produtos internos de phi_i e a funcao f descrita
    --> k      = altura do chip (h)
    --> xizes  = vetor de nos
    --> f_resp = lista polinomial (1D) correspondente a f
    '''
    r = []          # vetor d do sistema linear
    dequ = []       # diagonal principal de A
    for i in range(1,len(xizes)-1):
        phi_elem = 0

        phi_in = np.flip(np.polymul([1/k, -xizes[i-1]/k], [1/k, -xizes[i-1]/k]))
        phi_elem += integr(phi_in, xizes[i-1], xizes[i])

        phi_sp = np.flip(np.polymul([-1/k, xizes[i+1]/k], [-1/k, xizes[i+1]/k]))
        phi_elem += integr(phi_sp, xizes[i], xizes[i+1])

        dequ.append(phi_elem)

        # Vetor r
        r_elem = 0
        r_in = np.flip(np.polymul([1/k, -xizes[i-1]/k], f_resp))
        r_elem += integr(r_in, xizes[i-1], xizes[i])
        r_sp = np.flip(np.polymul([-1/k, xizes[i+1]/k], f_resp))
        r_elem += integr(r_sp, xizes[i], xizes[i+1])
        r.append(r_elem)

    ddif = []           # diagonal secundaria de A
    for i in range(1, len(xizes)-2):
        phisec = np.flip(np.polymul([-1/k, xizes[i+1]/k], [1/k, -xizes[i]/k]))
        ddif.append(integr(phisec, xizes[i], xizes[i+1]))

    return dequ, ddif, r

def decLU(t,dp,ds):
    '''
    Funcao que recebe a matriz tridiagonal A vetorizada entre:
     -> t  = tamanho da matriz
     -> dp = diag. principal
     -> ds = diag. secundaria
    e devolve as matrizes L e U da decomposicao LU de A.
    '''
    u = np.zeros(t)
    l = np.zeros(t-1)
    u[0] = dp[0]
    for i in range(1,t):
        l[i-1] = ds[i-1]/u[i-1]
        u[i] = dp[i] - l[i-1]*ds[i-1]
    return u,l

def resolutor(t,p,q,ds,r):
    '''
    Funcao que encontra a solucao do sistema Ax = d, tomando como parametros:
     -> t  = tamanho da matriz
     -> p  = vetor da matriz L da decomposicao LU de A
     -> q  = vetor da matriz U da decomposicao LU de A
     -> ds = diag. secundaria da matriz A
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

def phis(xizes, k):
    '''
    Funcao que parametriza os vetores de phi_i paras o intervalo x_i-1 a x_i+1, posteriormente para ser utilizada no calculo do erro.
    --> k      = altura do chip (h)
    --> xizes  = vetor de nos
    '''
    resp = []
    for i in range(1, len(xizes)-1):
        resp.append([[1/k, -xizes[i-1]/k], [-1/k, xizes[i+1]/k]])
    return resp

def erro(v, v_barra, xizes, opc):
    '''
    Funcao que calcula o erro da integracao numerica para cada no x_i
    --> v       = lista polinomial (1D) da funcao
            f(x) dada
    --> v_barra = lista polinomial (2D) dos elementos de phi_i
    --> xizes   = vetor de nos
    --> opc     = booleano indicando se deve
            haver fronteira nao homogenea
    '''
    if opc == True:
        fin = int(input('Digite a fronteira inferior: '))
        fsp = int(input('Digite a fronteira superior: '))
        cond = np.zeros(len(v_barra[0]))
        cond[0] = fin; cond[1] = fsp-fin
        v_barra = np.array(v_barra)+cond
    
    ret = []
    for i in range(len(v_barra)):
        ret.append(abs(func(v,xizes[i+1]) - func(v_barra,xizes[i+1]))[1])
    return ret, v_barra

def main():
    l = 1                       # Comprimento do chip [mm]
    n = int(input('Digite o numero de nos x_i: '))# Numero de nos
    h = l/(n+1)                 # Espessura do chip [mm]
    x = h*np.arange(0, n+2)     # Nos
    
    # VALIDACAO
    valc = int(input('''Digite o caso de validação 
    a ser exibido:
    (1) k(x) = 1    ; f(x) = 12x(1-x)-2
    (2) k(x) = e^x  ; f(x) = e^x+1
    '''))
    if valc == 1:
        f = [-12, 12, -2]
        k = 1
        u_sol = [0, 0.0, -1.0, 2.0, -1.0]
    elif valc == 2:
        f = [2]
        k = [1]
        u_sol = [0, 1]
        for j in range(7):
            # Expansao das funcoes em series de Taylor
            f.append(1/np.math.factorial(j+1))
            k.append(1/np.math.factorial(j+1))
            if j != 6:
                u_sol.append(((j+3)*(-1)**(j+1))/np.math.factorial(j+2))
        f = np.flip(f)

    a, b, d = cria_matriz(h, x, f)
    U, L = decLU(n,a,b)
    aph = resolutor(n,L,U,b,d)      # Vetor alpha_i
    phi_lst = np.array(phis(x, h))

    u_n_barra = []              # Vetor da solucao aproximada
    u_n_barra.append(aph[0]*phi_lst[0,0])
    for u in range(n-1):
        u_n_barra.append(aph[u]*phi_lst[u,1]+
        aph[u+1]*phi_lst[u+1,0])
    u_n_barra.append(aph[n-1]*phi_lst[n-1,1])

    # CONDICOES DE FRONTEIRA NAO HOMOGENEAS
    bo = bool(int(input('''Considerar condições de fronteira homogeneas?
    [0:SIM // 1:NAO] ''')))

    er, u_n_barra = erro(u_sol, u_n_barra, x, bo)

    # IMPRESSOES FINAIS
    print('''Vetor solucao do sistema linear 
     [phi_i]*[alpha_i] = d''')
    print(aph)
    print()
    print('''-- Matriz de coeficientes da funcao -- 
 u_n_barra calculada para cada no x_i''')
    print(np.array(u_n_barra))
    print()
    print('-- Erro medido para cada no x_i --')
    print(np.array(er))

main()