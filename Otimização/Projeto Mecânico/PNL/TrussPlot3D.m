function TrussPlot3D(coord,inci,cont,U,Tens,fator)

nnos = size(coord,1);
nel  = size(inci,1);

coordX = coord; % Coordenadas com o fator de escala
coord_r= coord; % Coordenadas reais

for i = 1:nnos 
    coordX(i,1) = coord(i,1) + fator*U(i,1);
    coordX(i,2) = coord(i,2) + fator*U(i,2);
    coordX(i,3) = coord(i,3) + fator*U(i,3);
    coord_r(i,1)= coord(i,1) + U(i,1);
    coord_r(i,2)= coord(i,2) + U(i,2);
    coord_r(i,3)= coord(i,3) + U(i,3);
end

A = zeros(max(nnos));
for i=1:nel
  A(inci(i,4),inci(i,4))=1;
  A(inci(i,5),inci(i,5))=1;
  A(inci(i,4),inci(i,5))=1;
  A(inci(i,5),inci(i,4))=1;
end

% Limites dos graficos
xmin = min(coord(:,1)); xmax = max(coord(:,1));
ymin = min(coord(:,2)); ymax = max(coord(:,2));
zmin = min(coord(:,3)); zmax = max(coord(:,3));

Lx = xmax - xmin; Ly = ymax - ymin; Lz = zmax - zmin;

xmin = xmin - 0.3*Lx; xmax = xmax + 0.3*Lx;
ymin = ymin - 0.3*Ly; ymax = ymax + 0.3*Ly;
ymin = ymin - 0.3*Ly; ymax = ymax + 0.3*Ly;

limits = [xmin xmax ymin ymax zmin zmax];

imax = find(Tens == max(Tens)); % Elemento com a maxima tensao

figure(1)
gplot3(A,coord,'o-');
axis(limits);
hold on;
% coord = coord_r;

%% PLOTANDO CONDICOES DE CONTORNO (APOIOS) %%

t=0.05*max(Lx,Ly);
for i=1:size(cont,1)
    if cont(i,2)==1
        x_map_color=[coord(cont(i,1),1) coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)+t/2*sqrt(3)];
        y_map_color=[coord(cont(i,1),2) coord(cont(i,1),2)+t/2 coord(cont(i,1),2)-t/2 ];
        fill(x_map_color,y_map_color,'k')
    end
    if cont(i,2)==2
        x_map_color=[coord(cont(i,1),1) coord(cont(i,1),1)+t/2 coord(cont(i,1),1)-t/2];
        y_map_color=[coord(cont(i,1),2) coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)-t/2*sqrt(3) ];
        fill(x_map_color,y_map_color,'k')
    end
end

%% PLOTANDO NUMERO DE ELEMENTOS %%

for i=1:nel;
   text((coord(inci(i,4),1)+coord(inci(i,5),1))/2,...
        (coord(inci(i,4),2)+coord(inci(i,5),2))/2,...
        (coord(inci(i,4),3)+coord(inci(i,5),3))/2,...
        num2str(i),...
        'EdgeColor','black','HorizontalAlignment','center',...
        'BackgroundColor',[.9 .9 .9],'FontSize',8);
end

%% PLOTANDO NUMERO DE NOS %%

for i=1:nnos;
   text(coord(i,1),coord(i,2),coord(i,3),num2str(i),'HorizontalAlignment',...
       'center','VerticalAlignment','bottom','FontSize',15);
end
axis equal;

%% PLOTANDO TRELICA DEFORMADA %%

figure(2)

% gplot3(A,coord_r,'--b');
axis(limits);

hold on;
for i = 1:nel

    no1 = inci(i,4); no2 = inci(i,5);

    xe1=[ coordX(no1,1), coordX(no2,1)];
    ye1=[ coordX(no1,2), coordX(no2,2)];  
    ze1=[ coordX(no1,3), coordX(no2,3)];  
    
    if i==imax
        plot3(xe1,ye1,ze1,'-k','LineWidth',1);%%
    else
        plot3(xe1,ye1,ze1,'-k','LineWidth',1);
    end     
end

for i = 1:nnos
    hold on;
    plot3(coordX(i,1),coordX(i,2),coordX(i,3),'ko','LineWidth',1.5)
end

coord = coord_r;
t=0.05*max(Lx,Ly);
for i=1:size(cont,1)
    if cont(i,2)==1
        x_map_color=[coord(cont(i,1),1) coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)+t/2*sqrt(3)];
        y_map_color=[coord(cont(i,1),2) coord(cont(i,1),2)+t/2 coord(cont(i,1),2)-t/2 ];
        fill(x_map_color,y_map_color,'k')
    end
    if cont(i,2)==2     
        x_map_color=[coord(cont(i,1),1) coord(cont(i,1),1)+t/2 coord(cont(i,1),1)-t/2];
        y_map_color=[coord(cont(i,1),2) coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)-t/2*sqrt(3) ];
        fill(x_map_color,y_map_color,'k')
    end
    if cont(i,2)==3     
        x_map_color=[coord(cont(i,1),1) coord(cont(i,1),1)+t/2 coord(cont(i,1),1)-t/2];
        y_map_color=[coord(cont(i,1),2) coord(cont(i,1),2) coord(cont(i,1),2) ];
        z_map_color=[coord(cont(i,1),3) coord(cont(i,1),3)-t/2*sqrt(3) coord(cont(i,1),3)-t/2*sqrt(3) ];
        fill3(x_map_color,y_map_color,z_map_color,'k')
    end
end
axis equal;
end
