function [c, ceq] = tensoes_maximas(x)

global sigma_max

[~, Tens] = trelica_FEA(x);

c = abs(Tens) - sigma_max;
ceq = [];

end