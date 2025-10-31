%==========================================================================
% OPTIMIZATION PROBLEM: MAXIMIZATION OF OBJECTIVE FUNCTION
% 
% Description: This script solves a constrained optimization problem to
%              find the parameter w0 that maximizes the given objective
%              function within specified bounds.
%
% Problem Formulation:
%   Maximize: f(w0) = (0.375 * w0) / (27057.6483 - 9.249849 * w0)
%   Subject to: 600 ≤ w0 ≤ 1366.05
%
% Note: Since fmincon performs minimization, we minimize the negative of
%       the objective function to achieve maximization.
%
% Author: [Your Name]
% Date: [Current Date]
% Version: 1.0
%==========================================================================

clear
clc

%% PROBLEM DEFINITION AND PARAMETERS
fprintf('Defining optimization problem...\n');

% Problem parameters (extracted as constants for clarity)
NUMERATOR_COEFFICIENT = 0.375;
CONSTANT_TERM = 27057.6483;
DENOMINATOR_COEFFICIENT = 9.249849;

% Optimization bounds
LOWER_BOUND = 600;
UPPER_BOUND = 1366.05;

%% OBJECTIVE FUNCTION DEFINITION
% Define the objective function to be maximized
% Note: fmincon minimizes, so we use negative for maximization
objectiveFunction = @(w0) -(NUMERATOR_COEFFICIENT * w0) / ...
                          (CONSTANT_TERM - DENOMINATOR_COEFFICIENT * w0);

% Analytical gradient (optional, for improved performance)
% gradientFunction = @(w0) -(NUMERATOR_COEFFICIENT * CONSTANT_TERM) / ...
%                          (CONSTANT_TERM - DENOMINATOR_COEFFICIENT * w0)^2;

%% CONSTRAINT DEFINITION
% Linear inequality constraints: A*w0 ≤ b
linearInequalityMatrix = [];
linearInequalityVector = [];

% Linear equality constraints: Aeq*w0 = beq
linearEqualityMatrix = [];
linearEqualityVector = [];

% Nonlinear constraints (none in this problem)
nonlinearConstraintFunction = [];

%% INITIAL GUESS
% Use midpoint of bounds as initial guess for better convergence
initialGuess = (LOWER_BOUND + UPPER_BOUND) / 2;

%% OPTIMIZATION OPTIONS
% Configure solver options for better performance and visibility
optimizationOptions = optimoptions('fmincon', ...
    'Display', 'iter', ...           % Show iteration progress
    'Algorithm', 'interior-point', ... % Robust algorithm for bound constraints
    'MaxFunctionEvaluations', 1000, ... % Limit function evaluations
    'MaxIterations', 100, ...        % Limit iterations
    'StepTolerance', 1e-8, ...       % Convergence tolerance
    'FunctionTolerance', 1e-8);      % Function value tolerance

%% SOLVE OPTIMIZATION PROBLEM
fprintf('Starting optimization process...\n');
fprintf('Problem bounds: [%.2f, %.2f]\n', LOWER_BOUND, UPPER_BOUND);
fprintf('Initial guess: %.4f\n\n', initialGuess);

try
    % Execute optimization
    [optimalSolution, optimalValue, exitFlag, output] = ...
        fmincon(objectiveFunction, initialGuess, ...
                linearInequalityMatrix, linearInequalityVector, ...
                linearEqualityMatrix, linearEqualityVector, ...
                LOWER_BOUND, UPPER_BOUND, ...
                nonlinearConstraintFunction, optimizationOptions);
    
    %% PROCESS RESULTS
    fprintf('\n=== OPTIMIZATION RESULTS ===\n');
    
    % Display optimal solution
    fprintf('Optimal w0: %.6f\n', optimalSolution);
    fprintf('Optimal objective value: %.6f\n', -optimalValue); % Convert back from negative
    
    % Calculate actual function value at optimum
    actualObjectiveValue = (NUMERATOR_COEFFICIENT * optimalSolution) / ...
                          (CONSTANT_TERM - DENOMINATOR_COEFFICIENT * optimalSolution);
    fprintf('Actual maximum value: %.6f\n', actualObjectiveValue);
    
    % Display solver information
    fprintf('\nSolver information:\n');
    fprintf('Exit flag: %d\n', exitFlag);
    fprintf('Number of iterations: %d\n', output.iterations);
    fprintf('Number of function evaluations: %d\n', output.funcCount);
    fprintf('Algorithm: %s\n', output.algorithm);
    
    % Interpret exit flag
    switch exitFlag
        case 1
            fprintf('Status: Converged to optimal solution.\n');
        case 0
            fprintf('Status: Maximum iterations reached.\n');
        case -2
            fprintf('Status: No feasible point found.\n');
        otherwise
            fprintf('Status: Check exit flag documentation.\n');
    end
    
    %% VALIDATION AND ANALYSIS
    fprintf('\n=== SOLUTION VALIDATION ===\n');
    
    % Check if solution is within bounds
    if optimalSolution >= LOWER_BOUND && optimalSolution <= UPPER_BOUND
        fprintf('✓ Solution within specified bounds.\n');
    else
        fprintf('✗ Solution outside bounds!\n');
    end
    
    % Check denominator to avoid division by zero
    denominator = CONSTANT_TERM - DENOMINATOR_COEFFICIENT * optimalSolution;
    if abs(denominator) > 1e-10
        fprintf('✓ Denominator is non-zero: %.6f\n', denominator);
    else
        fprintf('✗ Warning: Denominator接近零!\n');
    end
    
    %% PLOT RESULTS (Optional)
    % Create visualization of the objective function
    figure('Position', [100, 100, 800, 600], 'Name', 'Optimization Analysis');
    
    % Generate points for plotting
    plotPoints = linspace(LOWER_BOUND, UPPER_BOUND, 1000);
    objectiveValues = arrayfun(@(w0) (NUMERATOR_COEFFICIENT * w0) / ...
                          (CONSTANT_TERM - DENOMINATOR_COEFFICIENT * w0), plotPoints);
    
    % Plot objective function
    subplot(2,1,1);
    plot(plotPoints, objectiveValues, 'b-', 'LineWidth', 2);
    hold on;
    plot(optimalSolution, actualObjectiveValue, 'ro', 'MarkerSize', 8, ...
         'MarkerFaceColor', 'red', 'LineWidth', 2);
    grid on;
    xlabel('w0', 'FontSize', 11);
    ylabel('Objective Function Value', 'FontSize', 11);
    title('Objective Function and Optimal Solution', 'FontSize', 12, 'FontWeight', 'bold');
    legend('Objective Function', 'Optimal Solution', 'Location', 'best');
    
    % Plot convergence (if available)
    subplot(2,1,2);
    if isfield(output, 'firstorderopt')
        semilogy(1:output.iterations, output.firstorderopt, 'g-', 'LineWidth', 2);
        xlabel('Iteration', 'FontSize', 11);
        ylabel('First-Order Optimality', 'FontSize', 11);
        title('Convergence History', 'FontSize', 12, 'FontWeight', 'bold');
        grid on;
    else
        text(0.5, 0.5, 'Convergence data not available', ...
             'HorizontalAlignment', 'center', 'Units', 'normalized');
        title('Convergence History', 'FontSize', 12, 'FontWeight', 'bold');
    end
    
catch exception
    fprintf('\n❌ Optimization failed with error:\n');
    fprintf('%s\n', exception.message);
    fprintf('\nPlease check problem formulation and constraints.\n');
end

fprintf('\nOptimization process completed.\n');