% PNV3321 - 2022
clear all; close all;
clc;

% Chute inicial (Ci=[-10 10]')
Ci = [0 0]';

% Método de minimização multivariável sem restrições
% OBS: Declarar 'dfdx'

% [x,k] = MD_Gradiente(Ci); % Método do Gradiente
[x,k] = MD_Newton(Ci); % Método Newton - Também declarar 'df2dx2'

% Impressão dos resultados
fprintf('Ponto ótimo\n\n')
fprintf('x* = %f\n\n',x(:,end))
fprintf('Valor mínimo de f(x)\n')
fprintf('fmin = %f\n\n',f(x))

