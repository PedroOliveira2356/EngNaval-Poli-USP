%% Otimizacao trelica 3D %%

close all; clear; clc;

% Dados de entrada da treli�a 3D
DataMEF3D_25barDisc;

% Exemplo de an�lise da treli�a
% di�metros de cada barra
x = ones(25,1)*2;
% An�lise com os di�metros
[U, Tens] = trelica_FEA(x);
% plot da treli�a 3D
escala = 1e0;
TrussPlot3D(coord,inci,cont,U,Tens,escala)

% Escreve o otimizador aqui, com fmincon
% ...
% ...

