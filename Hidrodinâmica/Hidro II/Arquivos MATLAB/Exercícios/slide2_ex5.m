% Limpar workspace e figuras
clear; close all; clc;

%% Parâmetros para teste
U_values = [1, 2, 3];        % Velocidade da corrente livre
m_values = [1, 2, 5];        % Intensidade da fonte/sumidouro
a_values = [0.5, 1, 2];      % Posição da fonte/sumidouro

%% CASO (a): ϕ(x,y) = Ux + (m/2π) ln(√((x-a)² + y²))
figure('Position', [100, 100, 1200, 800]);

% Configuração 1: U=1, m=2, a=1
subplot(2, 3, 1);
U = 1; m = 2; a = 1;
phi_a = @(x,y) U*x + (m/(2*pi)) * log(sqrt((x-a).^2 + y.^2));
% Para ezplot, precisamos da função corrente implícita
ezplot(@(x,y) evaluate_psi_a(x,y,U,m,a), [-3, 3, -3, 3]);
title(sprintf('(a) U=%d, m=%d, a=%.1f', U, m, a));
xlabel('x'); ylabel('y'); axis equal; grid on;
hold on; plot(a, 0, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'red');

% Configuração 2: U=2, m=1, a=0.5
subplot(2, 3, 2);
U = 2; m = 1; a = 0.5;
ezplot(@(x,y) evaluate_psi_a(x,y,U,m,a), [-3, 3, -3, 3]);
title(sprintf('(a) U=%d, m=%d, a=%.1f', U, m, a));
xlabel('x'); ylabel('y'); axis equal; grid on;
hold on; plot(a, 0, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'red');

% Configuração 3: U=1, m=5, a=2
subplot(2, 3, 3);
U = 1; m = 5; a = 2;
ezplot(@(x,y) evaluate_psi_a(x,y,U,m,a), [-5, 5, -5, 5]);
title(sprintf('(a) U=%d, m=%d, a=%.1f', U, m, a));
xlabel('x'); ylabel('y'); axis equal; grid on;
hold on; plot(a, 0, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'red');

%% CASO (b): ϕ(x,y) = Ux + (m/2π)[ln(√((x+a)² + y²)) - ln(√((x-a)² + y²))]
% Configuração 1: U=1, m=2, a=1
subplot(2, 3, 4);
U = 1; m = 2; a = 1;
ezplot(@(x,y) evaluate_psi_b(x,y,U,m,a), [-3, 3, -3, 3]);
title(sprintf('(b) U=%d, m=%d, a=%.1f', U, m, a));
xlabel('x'); ylabel('y'); axis equal; grid on;
hold on; 
plot(-a, 0, 'bo', 'MarkerSize', 8, 'MarkerFaceColor', 'blue'); % Fonte
plot(a, 0, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'red');   % Sumidouro

% Configuração 2: U=2, m=1, a=0.5
subplot(2, 3, 5);
U = 2; m = 1; a = 0.5;
ezplot(@(x,y) evaluate_psi_b(x,y,U,m,a), [-3, 3, -3, 3]);
title(sprintf('(b) U=%d, m=%d, a=%.1f', U, m, a));
xlabel('x'); ylabel('y'); axis equal; grid on;
hold on; 
plot(-a, 0, 'bo', 'MarkerSize', 8, 'MarkerFaceColor', 'blue');
plot(a, 0, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'red');

% Configuração 3: U=1, m=5, a=2
subplot(2, 3, 6);
U = 1; m = 5; a = 2;
ezplot(@(x,y) evaluate_psi_b(x,y,U,m,a), [-5, 5, -5, 5]);
title(sprintf('(b) U=%d, m=%d, a=%.1f', U, m, a));
xlabel('x'); ylabel('y'); axis equal; grid on;
hold on; 
plot(-a, 0, 'bo', 'MarkerSize', 8, 'MarkerFaceColor', 'blue');
plot(a, 0, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'red');

sgtitle('Linhas de Corrente para Diferentes Potenciais de Velocidade');

%% Funções auxiliares para calcular a função corrente

% Função corrente para o caso (a)
function psi = evaluate_psi_a(x, y, U, m, a)
    % ψ(x,y) = Uy + (m/2π) * atan2(y, x-a)
    psi = U*y + (m/(2*pi)) * atan2(y, x-a);
end

% Função corrente para o caso (b)
function psi = evaluate_psi_b(x, y, U, m, a)
    % ψ(x,y) = Uy + (m/2π)[atan2(y, x+a) - atan2(y, x-a)]
    psi = U*y + (m/(2*pi)) * (atan2(y, x+a) - atan2(y, x-a));
end