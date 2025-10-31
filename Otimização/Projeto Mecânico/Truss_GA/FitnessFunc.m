function y = FitnessFunc(x)

global Z D vet_FO

Z = Z + 1; % Contador: Conta quantas vezes a função está sendo usada.

FO = 0; % Inicialização da Função Objetivo, FO.
for i = 1:D.nvars
   Le = D.csle(i,3); 
   FO = FO + Le*x(i)*D.RO; % FO = (L)(A)(p), (Comprimento)(Área)(densidade)
end

y = FO; % A função devolve a Função Objetivo (FO)

vet_FO(Z) = y;