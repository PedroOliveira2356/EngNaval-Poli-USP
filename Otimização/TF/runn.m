clear
clc

objetivo = @(w0) -(0.375*w0)/(27057.6483 - 9.249849*w0);

lb = 600;
ub = 1366.05;

A = [];
b = [];
Aeq = [];
beq = [];

x0 = (lb + ub)/2;

W = fmincon(objetivo,x0,A,b,Aeq,beq,lb,ub);