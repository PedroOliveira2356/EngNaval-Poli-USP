import numpy as np
import math

def func(x, y, item):
    '''
    Funcao que recebe as variaveis x e y e retorna o resultados para cada
    exemplo do EP
    --> x,y  = variaveis da funcao
    --> item = exemplo escolhido pelo usuario
    '''
    if item == '1.1':
        return 1
    if item == '1.2':
        return (x**2)/2 - x + 1/2
    if item == '2.1':
        return 1-x**2
    if item == '2.2':
        return math.sqrt(1-x)
    if item == '3.1':
        return math.sqrt((x**2+y**2)*math.e**(2*y/x)+x**4)/(x**2)
    if item == '3.2':
        return -x*(math.e**(x**2)-math.e**x)
    if item == '4.1':
        return 2*math.pi*x*(math.sqrt(1-x**2) - 3/4)
    if item == '4.2':
        return math.pi*(math.e**(-x**2))**2

def interp(vx, vw, m, M):
    '''
    Funcao que recebe um vetor de nos e pesos e os interpola
    devidamente para o intervalo [n, M]
    --> vx = vetor de nos
    --> vw = vetor de pesos
    --> m  = intervalo inferior
    --> M  = intervalo superior
    '''
    x_ret = []
    for i in range(len(vx)):
        x_ret.append(vx[i]*(M-m)/2 + (M+m)/2)
    x_ret = np.array(x_ret)

    vw = np.array(vw)
    w_ret = vw*(M-m)/2

    return x_ret, w_ret

def integr(s, nox, noy, coefx, coefy, item):
    '''
    Funcao que integra segundo as formulas de Gauss para s nos
    --> s            = numero de nos (6, 8 ou 10)
    --> nox, noy     = vetor de nos de x e y
    --> coefx, coefy = vetor de coeficientes de x e y
    --> item = exemplo escolhido pelo usuario
    '''
    if item != '3.1':
        A = 0
        for i in range(s):
            A += coefx[i]*func(nox[i], 0, item)
    else:
        A = 0
        for i in range(s):
            F = 0
            for j in range(s):
                F += coefy[j]*func(nox[i], noy[j], item)
            A += coefx[i]*F
    return A

def main():
    '''
    Funcao principal que imprime o numero de nos escolhido pelo usuario e
    o valor da integral calculada para cada caso.

    Pede-se para o usuário digitar o caso escolhido de acordo com uma lista e
    o numero de nos utilizados no calculo das integrais
    '''
    x1 =    [-0.9324695142031520278123016, -0.6612093864662645136613996, -0.2386191860831969086305017,
              0.2386191860831969086305017,  0.6612093864662645136613996,  0.9324695142031520278123016]
    w1 =    [ 0.1713244923791703450402961,  0.3607615730481386075698335,  0.4679139345726910473898703,
              0.4679139345726910473898703,  0.3607615730481386075698335,  0.1713244923791703450402961]
    
    x2 =    [-0.9602898564975362316835609, -0.7966664774136267395915539,
             -0.5255324099163289858177390, -0.1834346424956498049394761,
              0.1834346424956498049394761,  0.5255324099163289858177390, 
              0.7966664774136267395915539,  0.9602898564975362316835609]
    w2 =    [ 0.1012285362903762591525314,  0.2223810344533744705443560,
              0.3137066458778872873379622,  0.3626837833783619829651504,
              0.3626837833783619829651504,  0.3137066458778872873379622,
              0.2223810344533744705443560,  0.1012285362903762591525314]
    
    x3 =    [-0.9739065285171717200779640, -0.8650633666889845107320967, -0.6794095682990244062343274,
             -0.4333953941292471907992659, -0.1488743389816312108848260,
              0.1488743389816312108848260,  0.4333953941292471907992659,  0.6794095682990244062343274,
              0.8650633666889845107320967,  0.9739065285171717200779640]
    w3 =    [ 0.0666713443086881375935688,  0.1494513491505805931457763,  0.2190863625159820439955349,
              0.2692667193099963550912269,  0.2955242247147528701738930,
              0.2955242247147528701738930,  0.2692667193099963550912269,  0.2190863625159820439955349,
              0.1494513491505805931457763,  0.0666713443086881375935688]

    ex = str(input('''Digite o item do exemplo de acordo:
    1.1 -- Volume do cubo de aresta com compr. 1
    1.2 -- Volume do tetraedro de vertices dados
    2.1 -- Area da regiao do 1o quadr. abaixo da funcao 1-x^2
    2.2 -- Area da regiao do 1o quadr. abaixo da funcao (1-y)^1/2
    3.1 -- Area da superficie da funcao z = e^(y/x)
    3.2 -- Volume abaixo da funcao z = e^(y/x)
    4.1 -- Volume da calota esferica
    4.2 -- Volume do solido de revolucao 
    '''))

    n = int(input('Digite o valor do número de nos da integracao [6, 8, 10]: '))
    if n == 6:
        x = x1.copy()
        y = x1.copy()
        w = w1.copy()
    elif n == 8:
        x = x2.copy()
        y = x2.copy()
        w = w2.copy()
    elif n == 10:
        x = x3.copy()
        y = x3.copy()
        w = w3.copy()

    if ex == '1.1' or ex == '1.2' or ex == '2.1' or ex == '2.2':
        if ex == '1.1':
            print('Volume do cubo de aresta com compr. 1')
            print('funcao: f(x) = 1', end = '')
        if ex == '1.2':
            print('Volume do tetraedro de vertices dados')
            print('funcao: f(x) = (x^2)/2 - x + 1/2', end = '')
        if ex == '2.1':
            print('Area da regiao do 1o quadr. abaixo da funcao 1-x^2')
            print('funcao: f(x) = 1 - x^2', end = '')
        if ex == '2.2':
            print('Area da regiao do 1o quadr. abaixo da funcao (1-y)^1/2')
            print('funcao: f(x) = sqrt(1-x)', end = '')
        a, b = 0, 1
        print(f', {a} <= x <= {b}')
        x, wx = interp(x, w, a, b)
        I = integr(n, x, 0, wx, 0, ex)

    if ex == '3.1':
        print('Area da superficie da funcao z = e^(y/x)')
        print('funcao: f(x,y) = sqrt((x^2+y^2)*e^(2*y/x)+x^4)/(x^2)')
        a, b = 0.1, 0.5
        print(f'{a} <= x <= {b}')
        x, wx = interp(x, w, a, b)
        c, d = 0.001, 0.25
        print(f'x^3 <= y <= x^2')
        y, wy = interp(y, w, c, d)
        I = integr(n, x, y, wx, wy, ex)

    if ex == '3.2':
        print('Volume abaixo da funcao z = e^(y/x)')
        print('funcao: f(x) = -x(e^(x^2)-e^x)', end='')
        a, b = 0.1, 0.5
        print(f', {a} <= x <= {b}')
        x, wx = interp(x, w, a, b)
        I = integr(n, x, 0, wx, 0, ex)

    if ex == '4.1':
        print('Volume da calota esferica')
        print('funcao: f(x) = 2pi*x*(sqrt(1-x^2) - 3/4)', end='')
        a, b = 0, math.sqrt(7)/4
        print(f', {a} <= x <= %.2f'%b)
        x, wx = interp(x, w, a, b)
        I = integr(n, x, 0, wx, 0, ex)

    if ex == '4.2':
        print('Volume do solido de revolucao')
        print('funcao: f(y) = pi*(e^(-y^2))^2, -1 <= y <= 1')
        wx = w.copy()
        I = integr(n, x, 0, wx, 0, ex)

    print(f'Para n = {n}, o valor da integral calculada será {I}')

main()