function [tensao, ceq] = tensao_maxima(A)

global Fc sigma_a 

tensao = [Fc/A(1) - sigma_a;
          Fc/A(2) - sigma_a];
      
ceq = [];

end