%% ARQUIVO DE ENTRADA %% 

function D = DataMEF

%% COORDENADAS
 
%coord = [Xno Yno]
 coord = [ 0.00  0.00
           6.00  0.00
           0.00  0.25
           0.35  0.25
           0.35  0.35
           4.50  0.00 
           4.50  1.12
           3.00  0.00
           3.00  0.84
           1.50  0.00
           1.50  0.56
           0.35  0.00
           6.00  1.40 ];
 
%% INCIDENCIA
 
%inci = [elemento prop.mat. prop.geom.  nó i  nó j]
 
 inci = [   1        1        1        1        12
            2        1        1        12       10
            3        1        1        10       8
            4        1        1        8        6
            5        1        1        6        2
            6        1        1        3        4
            7        1        1        5        11
            8        1        1        11       9
            9        1        1        9        7
           10        1        1        7        13
           11        1        1        1        3
           12        1        1        1        4
           13        1        1        4        12
           14        1        1        4        5
           15        1        1        12       11
           16        1        1        11       10
           17        1        1        10       9
           18        1        1        8        9
           19        1        1        8        7
           20        1        1        7        6
           21        1        1        6        13
           22        1        1        13       2  
           23        1        1        4        11];
        
%% PROPRIEDADES DO MATERIAL
 
%  tmat=[E 
%        Poisson
%        rho];
 
tmat=[200e9
      0.3 
      0.1 ];
 
%% PROPRIEDADES GEOMÉTRICAS
 
% tgeo=[Área (m^2)
%       Momento de inércia (m^4)];
 
  tgeo=[  5e-4
          0.0001 ];
 
%% CONDIÇÕES DE CONTORNO
 
%cont=[n.do nó  GDL(U=1,V=2)]
 cont=[  1          2                      
         2          1            
         2          2 ];
 
%% FORÇAS
 
%loads=[n.do nó  GDL(U=1,V=2)  valor]
 loads=[   7          2        -2e3
           9          2        -2e3
           11         2        -2e3
           5          2        -1.5e3
           13         2        -1.5e3 ];

%% ALGORITMO GENÉTICO %%

nvars = size(inci,1);  
A = ones(1,nvars); % Valores iniciais das áreas
% AV - Áreas disponíveis
% AV = [1.62, 1.80, 1.99, 2.13, 2.38, 2.62, 2.88, 2.93, 3.09, 3.13, ...
%       3.38, 3.47, 3.55, 3.63, 3.84, 3.87, 3.88, 4.18, 4.22, 4.49, ...
%       4.59, 4.80, 4.97, 5.12, 5.94, 7.22, 7.97, 11.5, 13.50, 13.90, ...
%       14.2, 15.5, 16.0, 16.9, 18.8, 19.9, 22.0, 22.9, 28.5, 30.0, 33.5]; %in^2

TM = 235e6;   % Tensão limite admissível [Pa]
DM = 1e-3;    % Máximo deslocamento [m]    
RO = 77.01e3; % Massa específica [N/m^3]

csle = ones(nvars,3);

for i = 1:nvars
   noi = inci(i,4); % Nó inicial
   nof = inci(i,5); % Nó final
   dx = coord(nof,1) - coord(noi,1); % Diferença no eixo x
   dy = coord(nof,2) - coord(noi,2); % Diferença no eixo y
   Le = sqrt(dx*dx + dy*dy); % Comprimento da barra
   c = dx/Le;
   s = dy/Le;
   csle(i,1) = c;
   csle(i,2) = s;
   csle(i,3) = Le;
end

D = struct('coord',coord,'inci',inci,'tmat',tmat,'tgeo',tgeo,'cont',cont,...
           'loads',loads,'A',A','TM',TM','DM',DM','RO',RO',...
           'csle',csle,'nvars',nvars);    
    
    
    
    
    
    