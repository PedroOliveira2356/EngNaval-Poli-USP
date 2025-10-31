function [x,vet_FO,vet_TU] = GATruss()

global Z Z2 D vet_FO vet_TU

Z = 0;
Z2 = 0;
D = DataMEF;

nvars = D.nvars; % Número de barras
LB = 1e-4*ones(1,nvars); % Limite inferior
UB = 13e-4*ones(1,nvars);  % Limite superior %
ObjectiveFunction = @FitnessFunc;
ConstraintFunction = @ConstraintsFunc;
options = gaoptimset('PopulationSize',100,'TolFun',1e-6);
disp('Optimization in progress, please wait...')
% Run GA
[x,fval,~,~,~,~] = ga(ObjectiveFunction,nvars,[],[],[],[],LB,UB, ...
    ConstraintFunction,options);

% Display optimization results
disp('Optimization results:')
fprintf('Weight of best solution is: %6.8g\n',fval)
fprintf('Number of function evaluations: %d\n',Z)
disp('Best solution:')
disp(x')

end
