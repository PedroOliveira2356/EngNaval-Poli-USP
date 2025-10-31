% Busca pelo m�todo de Bisse��o
% Intervalo de entrada
% OBS: precisa declarar f(x) e dfdx

function [X,I] = Bissecao(I)

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
    
    % Novo ponto �timo pela bisse��o
    x(k+1) = (ak+bk)/2;
    mk = (ak+bk)/2;
    
    % Derivada avaliada em x(k+1)
    flinha = dfdx(mk);
    
    if (flinha == 0)
        break
    end

    % Novo intervalo
    if flinha > 0
        bk = mk;
    else
        ak = mk;
    end
    I = [ak bk];
    % Novo tamanho de intervalo
    Lk = bk-ak;
    
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