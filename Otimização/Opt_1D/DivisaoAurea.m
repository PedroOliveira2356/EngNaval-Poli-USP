% Busca pelo m�todo da Divis�o �urea
% Intervalo de entrada
% OBS: precisa declarar f(x)

function [X,I] = DivisaoAurea(I)

% Toler�nica Epslon
eps = 1e-5;  

% Pontos do intervalo
ak = I(1);
bk = I(2);

% Tamanho do intervalo
Lk = bk-ak;

% Solu��o (ponto �timo) x inicial
x(1) = (ak+bk)/2;

% Contador k
k = 1;

% Enquanto o intervalo � maior que a toler�ncia Epsilon
while (Lk > 2*eps)
    
    % Pontos da divis�o �urea
    vk = ak + 0.382*Lk;
    wk = ak + 0.618*Lk;
    
    % Fun��o objetivo avaliada em vk e wk
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

    % Novo ponto �timo
    x(k+1) = (ak+bk)/2;
    
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