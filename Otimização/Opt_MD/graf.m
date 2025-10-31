function graf(x)

%Plotando a curva no espaço 3D
figure(1)
a = max(abs([max(max(x(1,:)))-min(min(x(1,:))) max(max(x(2,:)))-min(min(x(2,:)))]))/5;

[Tx,Ty]=meshgrid([(min(min(x(1,:)))-a):((max(max(x(1,:)))-min(min(x(1,:)))+2*a)/50):(max(max(x(1,:)))+a)],[(min(min(x(2,:)))-a):((max(max(x(2,:)))-min(min(x(2,:)))+2*a)/50):(max(max(x(2,:)))+a)]);

surfc(Tx,Ty,(Tx.^2)+2*(Ty.^2)-2*Tx-Ty)

colorbar

%Plotando a solução a cada iteração
figure(2)
contour(Tx,Ty,(Tx.^2)+2*(Ty.^2)-2*Tx-Ty,20);
hold on
colorbar
title('Busca da solução')

for i = 1:size(x,2)
    plot(x(1,i),x(2,i),'k*')
end

for i = 1:(size(x,2)-1)
    line([x(1,i) x(1,i+1)],[x(2,i) x(2,i+1)],'Color',[0 0 0])
end



end