function plot_flow(P,X,Y)

[U,V] = gradient(P);
[hx, ~] = gradient(X);
[~, hy] = gradient(Y);

U = U./hx;
V = V./hy;

clf
hold on
%quiver(X,Y,U,V)

n_streams = 30;
streamline(X,Y,U,V,0.1+zeros(1,n_streams),linspace(Y(1,1),Y(end,end),n_streams))
streamline(X,Y,-U,-V,0.1+zeros(1,n_streams),linspace(Y(1,1),Y(end,end),n_streams))

contour(X,Y,P,n_streams,'r')
axis equal

end