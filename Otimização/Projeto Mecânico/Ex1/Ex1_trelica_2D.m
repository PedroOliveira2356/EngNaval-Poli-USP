% Otimizacao trelica 2D 

close all; clear all; clc;

global rho length Fc sigma_a 

rho = 2700;
length = 1;
Fc = 100e4;
sigma_a = 100e6;
Amin = [0.00001
        0.00001];

% chute inicial
A = [0.01
     0.01];

% option = optimset('Display','iter','Diagnostics','on');
option = optimset('Display','iter','Diagnostics','on','Algorithm','sqp');

[A, fval, flag, output, lambda] = ...
    fmincon('massa_trelica',A,[],[],[],[],Amin,[],'tensao_maxima',option);

A

% Encontrar raízes 
p = [1 -Amin(1) 0 sigma_a*Fc -Fc*Fc];
A1 = roots(p)

