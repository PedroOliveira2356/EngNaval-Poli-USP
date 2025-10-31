function [U, Tens] = trelica_FEA(x)

global coord cont inci loads tmat 

nnos=size(coord,1);
nel=size(inci,1);
ncont=size(cont,1);
ngdl=3;

id=ones(ngdl,nnos);
 
for i=1:ncont
    id(cont(i,2),cont(i,1))=0;
end

neq=0; % inicializando o numero de equacoes
for i=1:nnos
    for j=1:ngdl
        if id(j,i)==1
            neq=neq+1;
            id(j,i)=neq;
        end
    end
end 

F  = zeros(neq,1); % Inicialização do vetor Força
Kg = zeros(neq,neq); % Inicialização da Matriz de Rigidez

nloads=size(loads,1); % Contagem de cargas externas

% Cálculo do vetor força para para o sistema linear
% F = (GDL,nó)
for i=1:nloads
    if id(loads(i,2),loads(i,1))~=0
        F(id(loads(i,2),loads(i,1)),1)=loads(i,3);
    end
end

%% C�?LCULO DA MATRIZ DE RIGIDEZ GLOBAL KG %%

ngdel = 6; % numero de graus de liberdade do elemento
for i = 1:nel

    noi = inci(i,4); 
    noj = inci(i,5);
 
    x1 = coord(noi,1); x2 = coord(noj,1);
    y1 = coord(noi,2); y2 = coord(noj,2);
    z1 = coord(noi,3); z2 = coord(noj,3);
    
    Le = sqrt( (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2 );
    
    l = (x2 - x1)/Le;
    m = (y2 - y1)/Le;
    n = (z2 - z1)/Le;
      
    ntmat = inci(i,2);
    E = tmat(1,ntmat);
    
    matL = [l, m, n, 0, 0, 0
            0, 0, 0, l, m, n];
   
    A = pi*x(i)^2/4;
    
    ke = (E*A/Le)*(matL')*[1 -1;-1 1]*matL;    

       %[ u do noi   v do noi   u do noj   v do noj ]
    loc = [id(1,noi), id(2,noi), id(3,noi), id(1,noj), id(2,noj), id(3,noj)];

    for il=1:ngdel
        ilg=loc(il);
        if ilg~=0
            for ic=1:ngdel
                icg=loc(ic);
                if icg~=0
                    Kg(ilg,icg)=Kg(ilg,icg)+ke(il,ic);
                end
            end
        end
    end
    
end

%% VETOR SOLUÇÃO %%

X = Kg\F;

% U = [ Ux Uy ]
U = zeros(size(id,2),3);
for i = 1:size(id,2)
    for j = 1:3
        if id(j,i)~=0
            U(i,j) = X(id(j,i));
        end
    end
end

Tens=zeros(nel,1);
for i=1:nel
    
    noi = inci(i,4); 
    noj = inci(i,5);   
    
    u1 = U(noi,1); v1 = U(noi,2); w1 = U(noi,3);
    u2 = U(noj,1); v2 = U(noj,2); w2 = U(noj,3);
    
    vetdesloc = [u1; v1; w1; u2; v2; w2];
    
    x1 = coord(noi,1); x2 = coord(noj,1);
    y1 = coord(noi,2); y2 = coord(noj,2);
    z1 = coord(noi,3); z2 = coord(noj,3);
    
    Le = sqrt( (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2 );
    
    l = (x2 - x1)/Le;
    m = (y2 - y1)/Le;
    n = (z2 - z1)/Le;
      
    ntmat = inci(i,2);
    E = tmat(1,ntmat);
    
    matL = [l, m, n, 0, 0, 0
            0, 0, 0, l, m, n];    
        
    Tens(i) = E/Le*[-1 1]*matL*vetdesloc;
    
end
