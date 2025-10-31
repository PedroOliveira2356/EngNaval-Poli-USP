% Busca pelo m�todo da Divis�o �urea
% Intervalo de entrada
% OBS: precisa declarar f(x)

function [lambda,I] = DivisaoAurea_busca(I,x,d)

% Toler�nica Epslon
eps = 1e-5;  

% Pontos do intervalo
ak = I(1);
bk = I(2);

% Tamanho do intervalo
Lk = bk-ak;

% Solu��o (ponto �timo) x inicial
lambda(1) = (ak+bk)/2;

% Contador k
k = 1;

% Enquanto o intervalo � maior que a toler�ncia Epsilon
while (Lk > 2*eps)
    
    % Pontos da divis�o �urea
    vk = ak + 0.382*Lk;
    wk = ak + 0.618*Lk;
    
    % Fun��o objetivo avaliada em vk e wk
    fvk = f(x + vk*d);
    fwk = f(x + wk*d);
    
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
    lambda(k+1) = (ak+bk)/2;
    
    % Atualize o contador
    k = k + 1;

    % Break (evitar loop infinito)
    if (k == 100)
        disp('N�mero m�ximo de itera��es na busca unidimensional!')
        break
    end
end

% Ponto �timo
lambda = lambda(k);

end