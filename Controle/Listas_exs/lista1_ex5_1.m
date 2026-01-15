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
P = M*g;
y0 = (P/K)^(1/3);
keq = 3*K*y0^2;
tspan = [0 -2*M/B*log(0.001)]; %x/x0(t)~e^(-B/2M*t) == t~-2M/B*ln(x/x0)
init = [0 0];

%% SOLVING
[t1,y1] = ode45(@(t,y) odefun1(t,y,y0,M,B,K,f,P ),tspan,init);
[t2,y2] = ode45(@(t,y) odefun2(t,y, M,B, f,keq),tspan,init);

%% PLOTTING
plot(t1,y1(:,1),t2,y2(:,1));
xlabel(’t [s]’);
ylabel(’y(t) [m]’);
legend(’NON-LINER’,’LINEAR(IZED)’);

%% ODE FUNCTIONS
% NON-LINEAR SYSTEM
function dydt = odefun1(t,y,y0,M,B,K,f,P)
    dydt = zeros(2,1);
    dydt(1) = y(2);dydt(2) = (P+f(t)-B*y(2)-K*(y(1)+y0)^3)/M;
end
% LINEAR(IZED) SYSTEM
function dydt = odefun2(t,y,M,B,f,keq)
    dydt = zeros(2,1);
    dydt(1) = y(2);
    dydt(2) = (f(t)-B*y(2)-keq*y(1))/M;
end