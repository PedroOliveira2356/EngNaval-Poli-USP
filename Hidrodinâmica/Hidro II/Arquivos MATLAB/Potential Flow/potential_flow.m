xi = -1;
xf = 1;

yi = -0.5;
yf = 0.5;

nx = 51;
ny = 31;

x = linspace(xi,xf,nx);
y = linspace(yi,yf,ny);

P = zeros(ny,nx);

[X,Y] = meshgrid(x,y);

u = 1;
v = 0;

P = uniform_flow(P,X,Y,u,v);

q = 10;
x0 = -0.001;
y0 = 0.1;
P = source_flow(P,X,Y,x0,y0,q);

q = -10;
x0 = 0.001;
y0 = 0.1;
P = source_flow(P,X,Y,x0,y0,q);


q = 10;
x0 = -0.001;
y0 = -0.1;
P = source_flow(P,X,Y,x0,y0,q);

q = -10;
x0 = 0.001;
y0 = -0.1;
P = source_flow(P,X,Y,x0,y0,q);

plot_flow(P,X,Y)