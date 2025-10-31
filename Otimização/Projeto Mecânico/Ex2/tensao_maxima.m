function [tensao, ceq] = tensao_maxima(x)

global P E length

tensao = [P - ( ((pi^3)*E*(x(1)^3)*(x(2))) / (4*(length^2)))];
      
ceq = [];

end