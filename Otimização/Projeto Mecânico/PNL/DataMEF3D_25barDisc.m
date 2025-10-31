%% ARQUIVO DE ENTRADA %% 

global coord inci cont loads tmat tgeo sigma_max

%% COORDENADAS
 
%coord = [Xno Yno Zno]
 coord = [  -1.5,  0.0,  8.0 
             1.5,  0.0,  8.0
            -1.5,  1.5,  4.0
             1.5,  1.5,  4.0
             1.5, -1.5,  4.0
            -1.5, -1.5,  4.0
            -4.0,  4.0,  0.0
             4.0,  4.0,  0.0
             4.0, -4.0,  0.0
            -4.0, -4.0,  0.0 ]*12;

           
%% INCIDENCIA
 
%inci = [elemento prop.mat. prop.geom.  no i  no j]
 
 inci = [   1        1        1        1        2
            2        1        1        1        4
            3        1        1        2        3
            4        1        1        1        5
            5        1        1        2        6
            6        1        1        2        4
            7        1        1        2        5
            8        1        1        1        3
            9        1        1        1        6
           10        1        1        6        3
           11        1        1        5        4
           12        1        1        3        4
           13        1        1        6        5
           14        1        1        3       10
           15        1        1        6        7
           16        1        1        4        9
           17        1        1        5        8
           18        1        1        4        7
           19        1        1        3        8
           20        1        1        5       10
           21        1        1        6        9
           22        1        1        6       10
           23        1        1        3        7
           24        1        1        4        8
           25        1        1        5        9];
        
%% PROPRIEDADES DO MATERIAL
 
%  tmat=[E 
%        Poisson
%        rho];
 
tmat=[3e7
      0.3 
      7.3e-4 ];
 
%% PROPRIEDADES GEOMÉTRICAS
 
% tgeo=[Area (m^2)
%       Momento de inercia (m^4)];
%  d = 0.1;
  tgeo=[  pi
          0.0001 ];
     
%% CONDIÇÕES DE CONTORNO
 
%cont=[no  GDL(U=1,V=2)]
 cont=[  7          1                      
         7          2  
         7          3
         8          1  
         8          2
         8          3
         9          1
         9          2
         9          3
        10          1
        10          2
        10          3];
 
%% FORÇAS
 
%loads=[no  GDL(U=1,V=2)  valor]
 loads=[   1          2          60e3
           2          2          60e3];
       
sigma_max = 37e3/1.5;       
    