% Definir os parâmetros
M = 10; % Massa
B = 0.5; % Amortecimento
C = 0.5; 
y_r = 10; % Valor final

% Definir a equação diferencial de primeira ordem: M*dv/dt = -B*v + F

f = @(t, y) (-(B+C)*y + C*y_r)/M;

% @(t, y): definição de uma função que utiliza como entrada os valores t e
% y.


% Definir o intervalo de tempo (segundos)
tspan = [10 100];

% Definir as condições iniciais do navio para y
y0 = 0; 

% Resolver a equação diferencial utilizando a função ode45, com entrada a
% função f, intervalo de tempo tspan e as condições iniciais y0.
[t, y] = ode45(f, tspan, y0);

% Plot the results for y1
subplot(1, 1, 1);
plot(t, y(:, 1));
xlim([0, 100]);
ylim([0, 10]);
xlabel('Tempo');
ylabel('y(t)');
grid on;

% Adjust subplot layout
sgtitle('Solução da equação diferencial de primeira ordem');