% M�todo do gradiente (m�ximo descenso)
function [X,K] = MD_Gradiente(Ci)

% Toler�ncia
epsilon = 1e-4;

% C�lculo do gradiente da fun��o no chute inicial
gk = dfdx(Ci);

% Salvando o chute inicial (armazenamento de todos os pontos
x(1:length(Ci),1) = Ci;

% Contador
k = 0;

% Enquanto o gradiente for mais alto que epsilon
while norm(gk) > epsilon
    
    % Atualizar contador
    k = k + 1;
    
    % Limite m�ximo de itera��es
    if k > 300
        disp('Limite m�ximo de itera��es atingido. Solu��o n�o encontrada!')
        break
    end
    
    % Dire��o de descida (m�ximo descenso)
    dk = -gk;
    
    % Verifique se a dire��o � de descida, sen�o pare
    if dk'*gk > 0
        disp('Dire��o de subida tomada, ao inv�s da de descida!')
        break
    end
    
    % Intervalo de busca
    I = [0 10];
    % M�todo da Divis�o �urea
    lambda = DivisaoAurea_busca(I,x(1:length(Ci),k),dk);
%     lambda = 0.01;
    
    % Calculando novos pontos (salvando a solu��o ao longo de k)
    for i=1:length(Ci)
         x(i,k+1) = x(i,k) + lambda*dk(i);     %C�lculo dos novos pontos
    end
    
    % Novo gradiente
    gk = dfdx(x(1:length(Ci),k+1));
    
end

% Itera��es necess�rias
K = k-1;
% Ponto �timo
X = x(1:length(Ci),:);

% Gr�fico
graf(x)

end