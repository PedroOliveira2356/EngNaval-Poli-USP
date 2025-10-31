% PNV3321 - 2022
clear all; close all;
clc;

% Intervalo (I=[1 4])
I = [1 4];

% Ponto inicial (somente para Newton)
x0 = 1;

% Método de minimização unidimensional sem restrições
% OBS: Declarar 'f'

% [X] = DivisaoAurea(I) -> Método da Divisão Áurea
% [X] = Bisssecao(I) -> Método de Bisseção (declarar também dfdx)
% [X] = Newton1D(I) -> Método de Newton 1D (declarar também df2dx2 e x0)

% [X] = DivisaoAurea(I);
% [X] = Bissecao(I);
[X] = Newton1D(I,x0);


% Gerando o gráfico da função no intervalo
figure(2)
graf(I,X)
hold on
plot(X,f(X),'*')

% Impressão dos resultados
fprintf('Ponto ótimo\n')
fprintf('x* = %f\n\n',X)
fprintf('Valor mínimo de f(x)\n')
fprintf('fmin = %f\n\n',f(X))
grid on

