% Otimizacao trelica 2D 

close all; clear all; clc;

global rho length P E

rho = 2700;
length = 1;
P = 1e12;
E = 70e9;
xmax = [0.5
        0.05];
xmin = [0.02
        0.005];

% chute inicial
x = [0.10  % R
     0.01]; % t

% option = optimset('Display','iter','Diagnostics','on');
option = optimset('Display','iter','Diagnostics','on','Algorithm','sqp');

[x, fval, flag, output, lambda] = ...
    fmincon('massa_coluna',x,[],[],[],[],xmin,xmax,'tensao_maxima',option);

x