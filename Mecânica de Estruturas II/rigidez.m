%Matriz rigidez de elemento isoparam�trico de 4 n�s. Integra��o usando 4
%pontos Gaussianos
%dados entrada
% espessura
clc
clf
clear all
t = 1; % mm
% number of Gauss points
ngps = 4 ;
% coordenadas xi,yi
x = [2 5 4 1]; % [2 5 4 1]  [3 5 5 3] [2 5 5 2]
y= [1 2 6 4];  % [1 2 6 4]  [2 2 4 4] [1 1 6 6]
plot([x 2],[y 1],'ko-','LineWidth',3,...
'MarkerSize',12,...
'MarkerEdgeColor','k')
xlim([0 7])
ylim([0 7])
xlabel('x (mm)')
ylabel ('y (mm)')
% matriz elastica
E = 1.0;
nu = 0.25;
%Plane strain
%D = E/((1+nu)(1-2nu))[1-nu nu 0;nu 1-nu 0;0 0 (1-2nu)/2];
%Plane stress
D = E*[1/(1-nu^2) nu/(1-nu^2) 0;nu/(1-nu^2) 1/(1-nu^2) 0;0 0 1/(2*(1+nu))];
% shape functions and its derivatives
syms eta xi
% N1
N1= 0.25*((1-eta)(1-xi));
dN1_eta=diff(N1,eta);
dN1_xi=diff(N1,xi);
% N2
N2= 0.25((1-eta)(1+xi));
dN2_eta=diff(N2,eta);
dN2_xi=diff(N2,xi);
% N3
N3= 0.25((1+eta)(1+xi));
dN3_eta=diff(N3,eta);
dN3_xi=diff(N3,xi);
% N4
N4= 0.25((1+eta)(1-xi));
dN4_eta=diff(N4,eta);
dN4_xi=diff(N4,xi);
%Matriz N
N_shape= [N1 N2 N3 N4];
% coordenadas de elemento como fun��o de eta, xi
xx=N_shapex';
yy=N_shapey';
% Pontos Gauss
eta1 = 0.5;
xi1 =0.5;
x1=[xi1 eta1];
% Evaluates the coordenates, Strain Matrix and Jacobian matrix at the specified Gauss point
xxx = double( subs(xx,[xi eta],x1) )
yyy = double( subs(yy,[xi eta],x1) )
% Matriz Jacobiana
Je=[dN1_xi dN2_xi dN3_xi dN4_xi;dN1_eta dN2_eta dN3_eta dN4_eta][x' y']
% Inverse of Jacobian
Je_inv = inv(Je);
Det_Je = det(Je)
%FUN = matlabFunction(Je);  % This creates a function handle
%y = feval(FUN, x0);         % Evaluates the new function handle at the specified points
%
% matrix of xi,eta derivatives of shape function
row1_dNi = [dN1_xi 0 dN2_xi 0 dN3_xi 0 dN4_xi 0];
row2_dNi = [dN1_eta 0 dN2_eta 0 dN3_eta 0 dN4_eta 0];
row3_dNi = [0 dN1_xi 0 dN2_xi 0 dN3_xi 0 dN4_xi];
row4_dNi = [0 dN1_eta 0 dN2_eta 0 dN3_eta 0 dN4_eta];
dNi = [row1_dNi;row2_dNi;row3_dNi;row4_dNi];
% x, y derivatives of shape functions 2x4
% Strain Matrix
AUX1 = zeros(2);
AUX= [Je_inv AUX1;AUX1 Je_inv];
B = [1 0 0 0;0 0 0 1; 0 1 1 0]AUXdNi
eta2=-1:0.25:1;
xi2=-1:0.25:1;
[X,Y] = meshgrid(eta2,xi2);
for i=1:length(xi2)
for j=1:length(eta2)
x1= [xi2(i) eta2(j)];
%double( subs(N_shape,[xi eta],x1))
%double( subs(N_shape,[xi eta],x1))
XX(i,j)=double( subs(N_shape,[xi eta],x1))[x'];
YY(i,j)=double( subs(N_shape,[xi eta],x1))[y'];
%pause
end