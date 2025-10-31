% PNV3321 - 2022
clear all; close all;
clc;

% Intervalo (I=[1 4])
I = [1 4];

% Ponto inicial (somente para Newton)
x0 = 1;

% M�todo de minimiza��o unidimensional sem restri��es
% OBS: Declarar 'f'

% [X] = DivisaoAurea(I) -> M�todo da Divis�o �urea
% [X] = Bisssecao(I) -> M�todo de Bisse��o (declarar tamb�m dfdx)
% [X] = Newton1D(I) -> M�todo de Newton 1D (declarar tamb�m df2dx2 e x0)

% [X] = DivisaoAurea(I);
% [X] = Bissecao(I);
[X] = Newton1D(I,x0);


% Gerando o gr�fico da fun��o no intervalo
figure(2)
graf(I,X)
hold on
plot(X,f(X),'*')

% Impress�o dos resultados
fprintf('Ponto �timo\n')
fprintf('x* = %f\n\n',X)
fprintf('Valor m�nimo de f(x)\n')
fprintf('fmin = %f\n\n',f(X))
grid on

