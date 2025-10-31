% Busca pelo método da Divisão Áurea
% Intervalo de entrada
% OBS: precisa declarar f(x)

function [X,I] = DivisaoAurea(I)

% Tolerânica Epslon
eps = 1e-5;  

% Pontos do intervalo
ak = I(1);
bk = I(2);

% Tamanho do intervalo
Lk = bk-ak;

% Solução (ponto ótimo) x inicial
x(1) = (ak+bk)/2;

% Contador k
k = 1;

% Enquanto o intervalo é maior que a tolerância Epsilon
while (Lk > 2*eps)
    
    % Pontos da divisão áurea
    vk = ak + 0.382*Lk;
    wk = ak + 0.618*Lk;
    
    % Função objetivo avaliada em vk e wk
    fvk = f(vk);
    fwk = f(wk);
    
    % Novo intervalo
    if fvk < fwk
        bk = wk;
    else
        ak = vk;
    end
    I = [ak bk];
    % Novo tamanho de intervalo
    Lk = bk-ak;

    % Novo ponto ótimo
    x(k+1) = (ak+bk)/2;
    
    % Atualize o contador
    k = k + 1;

    % Break (evitar loop infinito)
    if (k == 100)
        break
    end
end

% Ponto ótimo
X = x(k);

% Número de iterações
it = 0:(k-1);

plot(it,x);
grid
title('Busca da solução')
xlabel('Iterações')
ylabel('x*')

end