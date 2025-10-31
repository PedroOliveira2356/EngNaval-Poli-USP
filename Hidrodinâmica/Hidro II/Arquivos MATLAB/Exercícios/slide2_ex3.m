% Limpar workspace e figuras
clear; close all; clc;

% Definir diferentes valores de gamma (intensidade do vórtice)
gammas = [-4, -2, -1, 1, 2, 4];

% Criar uma nova figura
figure;

% Loop através dos diferentes valores de gamma
for i = 1:length(gammas)
    gamma = gammas(i);
    
    % Criar subplot para cada valor de gamma
    subplot(2, 3, i);
    
    % Definir a função corrente para o vórtice
    % psi = (gamma/(2*pi)) * log(sqrt(x^2 + y^2))
    if gamma >= 0
        psi_str = sprintf('(%d/(2*pi)) * log(sqrt(x^2 + y^2))', gamma);
    else
        psi_str = sprintf('(%d/(2*pi)) * log(sqrt(x^2 + y^2))', gamma);
    end
    
    % Usar ezplot para desenhar as linhas de corrente
    ezplot(psi_str, [-5, 5, -5, 5]);
    
    % Adicionar título e labels
    title(sprintf('Vórtice \\Gamma = %d', gamma));
    xlabel('x');
    ylabel('y');
    axis equal;
    grid on;
    
    % Adicionar ponto do vórtice na origem
    hold on;
    plot(0, 0, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'red');
end

% Ajustar o layout
sgtitle('Linhas de Corrente para Vórtice em (0,0) para Diferentes Valores de \Gamma');