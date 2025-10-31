% Busca pelo m�todo de Newton 1D
% Intervalo de entrada
% OBS: precisa declarar f(x), dfdx e df2dx2

function [X,I] = Newton1D(I,x0)

% Toler�nica Epslon para converg�ncia do ponto
eps = 1e-5;  

% Solu��o (ponto �timo) x inicial
x(1) = x0;

% Contador k
k = 1;

% Auxiliary variable for convergence
converged = 0; % == 0, did not converged yet, == 1 converged

% Enquanto o intervalo � maior que a toler�ncia Epsilon
while (converged == 0)
    
    % Novo ponto �timo por Newton
    x(k+1) = x(k) - dfdx(x(k))/df2dx2(x(k));

    % An�lise de converg�ncia
    if ((x(k+1)-x(k))/x(k+1) <= eps)
        converged = 1;
    end
    
    % Atualize o contador
    k = k + 1;

    % Break (evitar loop infinito)
    if (k == 100)
        break
    end
end

% Ponto �timo
X = x(k);

% N�mero de itera��es
it = 0:(k-1);

plot(it,x);
grid
title('Busca da solu��o')
xlabel('Itera��es')
ylabel('x*')

end