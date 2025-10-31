% PNV3321 - 2022
clear all; close all;
clc;

% Chute inicial (Ci=[-10 10]')
Ci = [0 0]';

% M�todo de minimiza��o multivari�vel sem restri��es
% OBS: Declarar 'dfdx'

% [x,k] = MD_Gradiente(Ci); % M�todo do Gradiente
[x,k] = MD_Newton(Ci); % M�todo Newton - Tamb�m declarar 'df2dx2'

% Impress�o dos resultados
fprintf('Ponto �timo\n\n')
fprintf('x* = %f\n\n',x(:,end))
fprintf('Valor m�nimo de f(x)\n')
fprintf('fmin = %f\n\n',f(x))

