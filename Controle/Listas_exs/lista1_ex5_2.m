%% INPUTS
% PARAMETERS
g=9.81; %m/s^2
M = 10; %kg
B = 16; %Ns/s
K = 40; %N/m^3

% EXITATION FORCE
A = 20;
f = @(t) A*cos(t);

%% CALCULATIONS
tspan = [0 -2*M/B*log(0.001)]; %x/x0(t)~e^(-B/2M*t) == t~-2M/B*ln(x/x0)
x0 = [0 0];

% FOR THE ACCURATE LINEARIZATION
delta = (A/K)^(1/3); % good estimate
% "E_spring = Fk(x)*x = Fk_lin(x)*x"
% when x0=0, oscillating according to delta*cos(t):
% <k*delta^3*delta>=<keq*delta*delta>=>k*(3/8)*delta^4=keq*(1/2)*delta^2
Keq = K*(3/4)*delta^2;

%% SOLVING
[t1,x1] = ode45(@(t,x) odefun1(t,x,M,B,K, f),tspan,x0);
[t2,x2] = ode45(@(t,x) odefun2(t,x,M,B, f),tspan,x0);
[t3,x3] = ode45(@(t,x) odefun3(t,x,M,B,Keq,f),tspan,x0);

%% PLOTTING
plot(t1,x1(:,1),t2,x2(:,1),t3,x3(:,1));
xlabel(’t [s]’);
xlabel(’x(t) [m]’);
legend(’NON-LINER’,’LINEAR (DUMB)’,’LINEAR (BETTER)’);

%% ODE FUNCTIONS
% NON-LINEAR SYSTEM
function dxdt = odefun1(t,x,M,B,K,f)
    dxdt = zeros(2,1);
    dxdt(1) = x(2);
    dxdt(2) = (f(t)-B*x(2)-K*x(1)^3)/M;
end

% LINEARIZED SYSTEM (DUMB)
function dxdt = odefun2(t,x,M,B,f)
    dxdt = zeros(2,1);
    dxdt(1) = x(2);
    dxdt(2) = (f(t)-B*x(2))/M;
end
% LINEARIZED SYSTEM (BETTER)
function dxdt = odefun3(t,x,M,B,Keq,f)
    dxdt = zeros(2,1);
    dxdt(1) = x(2);
    dxdt(2) = (f(t)-B*x(2)-Keq*x(1))/M;
end