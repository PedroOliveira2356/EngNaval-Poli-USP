%% Otimizacao trelica 3D %%

close all; clear; clc;

% Dados de entrada da treliça 3D
DataMEF3D_25barDisc;

% Exemplo de análise da treliça
% diâmetros de cada barra
x = ones(25,1)*2;
% Análise com os diâmetros
[U, Tens] = trelica_FEA(x);
% plot da treliça 3D
escala = 1e0;
TrussPlot3D(coord,inci,cont,U,Tens,escala)

% Escreve o otimizador aqui, com fmincon
% ...
% ...

