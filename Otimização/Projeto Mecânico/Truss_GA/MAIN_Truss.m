% Programa para otimização de treliça via Algoritmo Genético
clear; clc; close all;

% Contador de tempo (instante inicial)
tic;

% Montagem e solução do problema via GA
[x,vet_FO,vet_TU] = GATruss();

% Fator de escala para plot da estrutura deformada
fator = 100;
% Análise por MEF para plot final
[U,Tens] = Truss_MEF(x);
% plot final
Truss_plot(x,U,Tens,fator);

% Contador de tempo (instante final)
toc;