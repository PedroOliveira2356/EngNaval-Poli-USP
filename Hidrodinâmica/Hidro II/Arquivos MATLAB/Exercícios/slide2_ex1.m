% Exercício 1: Linhas de corrente de uma fonte/sorvedouro
% Localizada no ponto (0,0) para diferentes valores de m

clear all; close all; clc;

% Definir a função potencial de corrente para fonte/sorvedouro
% Para uma fonte/sorvedouro 2D, a função corrente é: ψ = m * θ / (2π)
% Onde θ = atan2(y,x) e m é a intensidade da fonte (m>0) ou sorvedouro (m<0)

% Valores de m para testar (positivo = fonte, negativo = sorvedouro)
valores_m = [-2, -1, -0.5, 0.5, 1, 2];

% Criar figura
figure('Position', [100, 100, 1200, 800]);

for i = 1:length(valores_m)
    m = valores_m(i);
    
    % Criar subplot
    subplot(2, 3, i);
    
    % Definir a função corrente
    if m >= 0
        titulo = sprintf('Fonte: m = %.1f', m);
    else
        titulo = sprintf('Sorvedouro: m = %.1f', m);
    end
    
    % Usar ezplot para a função corrente implícita
    % Para uma fonte/sorvedouro, as linhas de corrente são raios saindo da origem
    % A função corrente é constante ao longo de cada raio
    
    % Definir domínio
    xmin = -3; xmax = 3;
    ymin = -3; ymax = 3;
    
    % Plotar usando abordagem paramétrica para melhor visualização
    theta = linspace(0, 2*pi, 20); % Ângulos para as linhas de corrente
    r = linspace(0.1, 3, 10); % Raio (evitar r=0)
    
    hold on;
    
    % Plotar linhas de corrente (raios)
    for j = 1:length(theta)
        x_line = r * cos(theta(j));
        y_line = r * sin(theta(j));
        
        if m >= 0
            plot(x_line, y_line, 'b-', 'LineWidth', 1.5);
        else
            plot(x_line, y_line, 'r-', 'LineWidth', 1.5);
        end
    end
    
    % Marcar a origem
    plot(0, 0, 'ko', 'MarkerSize', 8, 'MarkerFaceColor', 'k');
    
    % Configurações do gráfico
    axis equal;
    xlim([xmin, xmax]);
    ylim([ymin, ymax]);
    title(titulo, 'FontSize', 12);
    xlabel('x');
    ylabel('y');
    grid on;
    
    hold off;
end

% Adicionar título principal
sgtitle('Linhas de Corrente - Fonte/Sorvedouro em (0,0)', 'FontSize', 14, 'FontWeight', 'bold');

% Método alternativo usando função implícita com ezplot
figure('Position', [100, 100, 1200, 400]);

% Exemplo com m = 1 (fonte)
subplot(1, 2, 1);
syms x y
psi = atan2(y,x); % Função corrente para m=1
ezplot(psi == -pi:pi/4:pi, [-3, 3, -3, 3]);
title('Fonte: m = 1 (ezplot)');
axis equal;
grid on;

% Exemplo com m = -1 (sorvedouro)
subplot(1, 2, 2);
ezplot(psi == -pi:pi/4:pi, [-3, 3, -3, 3]);
title('Sorvedouro: m = -1 (ezplot)');
axis equal;
grid on;

% Método usando contour para visualização alternativa
figure('Position', [100, 100, 800, 600]);

% Criar grid
[x_grid, y_grid] = meshgrid(linspace(-3, 3, 50), linspace(-3, 3, 50));

% Calcular função corrente para diferentes valores de m
m_test = [1, -1];
for k = 1:2
    subplot(1, 2, k);
    m = m_test(k);
    
    % Função corrente
    psi_grid = m * atan2(y_grid, x_grid);
    
    % Plotar curvas de nível (linhas de corrente)
    contour(x_grid, y_grid, psi_grid, 20, 'LineWidth', 1.5);
    
    if m > 0
        title(sprintf('Fonte: m = %d', m));
        colormap(jet);
    else
        title(sprintf('Sorvedouro: m = %d', m));
        colormap(cool);
    end
    
    axis equal;
    xlabel('x');
    ylabel('y');
    grid on;
    colorbar;
end

sgtitle('Visualização com Curvas de Nível', 'FontSize', 14);