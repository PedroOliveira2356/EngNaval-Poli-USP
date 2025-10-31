% Método do gradiente (máximo descenso)
function [X,K] = MD_Gradiente(Ci)

% Tolerância
epsilon = 1e-4;

% Cálculo do gradiente da função no chute inicial
gk = dfdx(Ci);

% Salvando o chute inicial (armazenamento de todos os pontos
x(1:length(Ci),1) = Ci;

% Contador
k = 0;

% Enquanto o gradiente for mais alto que epsilon
while norm(gk) > epsilon
    
    % Atualizar contador
    k = k + 1;
    
    % Limite máximo de iterações
    if k > 300
        disp('Limite máximo de iterações atingido. Solução não encontrada!')
        break
    end
    
    % Direção de descida (máximo descenso)
    dk = -gk;
    
    % Verifique se a direção é de descida, senão pare
    if dk'*gk > 0
        disp('Direção de subida tomada, ao invés da de descida!')
        break
    end
    
    % Intervalo de busca
    I = [0 10];
    % Método da Divisão Áurea
    lambda = DivisaoAurea_busca(I,x(1:length(Ci),k),dk);
%     lambda = 0.01;
    
    % Calculando novos pontos (salvando a solução ao longo de k)
    for i=1:length(Ci)
         x(i,k+1) = x(i,k) + lambda*dk(i);     %Cálculo dos novos pontos
    end
    
    % Novo gradiente
    gk = dfdx(x(1:length(Ci),k+1));
    
end

% Iterações necessárias
K = k-1;
% Ponto ótimo
X = x(1:length(Ci),:);

% Gráfico
graf(x)

end