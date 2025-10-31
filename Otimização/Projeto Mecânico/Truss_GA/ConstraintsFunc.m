function [c, ceq] = ConstraintsFunc(x)

global D Z2 vet_TU

Z2 = Z2 + 1;
ceq = [];
D.A = x';

nnos = size(D.coord,1);
nel = size(D.inci,1);
ncont = size(D.cont,1);
ngdl = 2;

id = ones(ngdl,nnos);
 
for i = 1:ncont
    id(D.cont(i,2),D.cont(i,1)) = 0;
end

neq = 0; % inicializando o numero de equacoes
for i = 1:nnos
    for j = 1:ngdl
        if id(j,i) == 1
            neq = neq+1;
            id(j,i) = neq;
        end
    end
end

F = zeros(neq,1); % Inicialização do vetor Força
Kg = zeros(neq,neq); % Inicialização da Matriz de Rigidez

nloads = size(D.loads,1); % Contagem de cargas externas

% Cálculo do vetor força para para o sistema linear
% F = (GDL,nó)
for i = 1:nloads
    if id(D.loads(i,2),D.loads(i,1)) ~= 0
        F(id(D.loads(i,2),D.loads(i,1)),1) = D.loads(i,3);
    end
end

%% CÁLCULO DA MATRIZ DE RIGIDEZ GLOBAL KG %%

ngdel = 4; % numero de graus de liberdade do elemento
for i = 1:nel

    noi = D.inci(i,4); 
    noj = D.inci(i,5);
 
    c = D.csle(i,1);
    s = D.csle(i,2);
    Le = D.csle(i,3);
    
    ntmat = D.inci(i,2);

    E = D.tmat(1,ntmat);
%     LB
    ke = (E*D.A(i)/Le)*[c*c   c*s -c*c -c*s
                      c*s   s*s -c*s -s*s
                     -c*c  -c*s  c*c  c*s
                     -c*s  -s*s  s*c  s*s];

       %[ u do noi   v do noi   u do noj   v do noj ]
    loc = [id(1,noi)  id(2,noi)   id(1,noj)  id(2,noj)];

    for il = 1:ngdel
        ilg = loc(il);
        if ilg ~= 0
            for ic = 1:ngdel
                icg = loc(ic);
                if icg ~= 0
                    Kg(ilg,icg) = Kg(ilg,icg)+ke(il,ic);
                end
            end
        end
    end
    
end

%% VETOR SOLUÇÃO %%

X = Kg\F;

% U = [ Ux Uy ]
U = zeros(size(id,2),2);
for i = 1:size(id,2)
    for j = 1:2
        if id(j,i) ~= 0
            U(i,j) = X(id(j,i));
        end
    end
end

Tens = zeros(nel,1);
for i = 1:nel
    
    xa = U(D.inci(i,4),1); xb = U(D.inci(i,4),2);
    xc = U(D.inci(i,5),1); xd = U(D.inci(i,5),2);
    
    c = D.csle(i,1);
    s = D.csle(i,2);
    Le = D.csle(i,3);
    
    ntmat = D.inci(i,2);

    E = D.tmat(1,ntmat);
    
    Vet_desloc = [xa;xb;xc;xd];

    Tens(i) = E/Le*[-c -s c s]*Vet_desloc;
    
end

vet_TU(Z2,1) = max(abs(Tens));
vet_TU(Z2,2) = max(max(abs(U)));

TS = Tens/D.TM -1;
US = abs(U)/D.DM - 1;
PS = sum(TS.*(TS>0));
PD = sum(US.*(US>0),2);
c = [PS; PD];


