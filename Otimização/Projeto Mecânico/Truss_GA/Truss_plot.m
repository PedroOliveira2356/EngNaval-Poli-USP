function Truss_plot(x,U,Tens,fator)

global D

coord = D.coord;
inci  = D.inci;
cont  = D.cont;
loads = D.loads;

nnos = size(coord,1);
nel  = size(inci,1);

coordX  = D.coord; % Coordenadas com o fator de escala
coord_r = D.coord; % Coordenadas reais

for i = 1:nnos 
    coordX(i,1)  = D.coord(i,1) + fator*U(i,1);
    coordX(i,2)  = D.coord(i,2) + fator*U(i,2);
    coord_r(i,1) = D.coord(i,1) + U(i,1);
    coord_r(i,2) = D.coord(i,2) + U(i,2);
end

A = zeros(max(nnos));
for i = 1:nel
  A(inci(i,4),inci(i,4)) = 1;
  A(inci(i,5),inci(i,5)) = 1;
  A(inci(i,4),inci(i,5)) = 1;
  A(inci(i,5),inci(i,4)) = 1;
end

% Limites dos graficos
xmin = min(coord(:,1)); xmax = max(coord(:,1));
ymin = min(coord(:,2)); ymax = max(coord(:,2));
Lx = xmax-xmin; Ly = ymax-ymin;
xmin = xmin-0.3*Lx; xmax = xmax+0.3*Lx;
ymin = ymin-0.3*Ly; ymax = ymax+0.3*Ly;

limits = [xmin xmax ymin ymax];

imax = find(Tens == max(Tens)); % Elemento com a maxima tensao

figure(1)
gplot(A,coord_r,'o-');
axis(limits);
hold on;
coord = coord_r;

%% PLOTANDO CONDICOES DE CONTORNO (APOIOS) %%

t = 0.05*max(Lx,Ly);
for i = 1:size(cont,1)
    if cont(i,2) == 1
        xe1 = [coord(cont(i,1),1) coord(cont(i,1),1)+t/2*sqrt(3)];
        ye1 = [coord(cont(i,1),2) coord(cont(i,1),2)+t/2];
        plot(xe1,ye1,'k','LineWidth',1.5);
    
        xe2 = [coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)+t/2*sqrt(3)];
        ye2 = [coord(cont(i,1),2)+t/2 coord(cont(i,1),2)-t/2];
        plot(xe2,ye2,'k','LineWidth',1.5); 
    
        xe3 = [coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)];
        ye3 = [coord(cont(i,1),2)-t/2 coord(cont(i,1),2)];
        plot(xe3,ye3,'k','LineWidth',1.5);
        
        x_map_color=[coord(cont(i,1),1) coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)+t/2*sqrt(3)];
        y_map_color=[coord(cont(i,1),2) coord(cont(i,1),2)+t/2 coord(cont(i,1),2)-t/2 ];
        fill(x_map_color,y_map_color,'k')
    end
    if cont(i,2) == 2
        xe1 = [coord(cont(i,1),1) coord(cont(i,1),1)+t/2];
        ye1 = [coord(cont(i,1),2) coord(cont(i,1),2)-t/2*sqrt(3)];
        plot(xe1,ye1,'k','LineWidth',1.5);
    
        xe2 = [coord(cont(i,1),1)+t/2 coord(cont(i,1),1)-t/2];
        ye2 = [coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)-t/2*sqrt(3)];
        plot(xe2,ye2,'k','LineWidth',1.5); 
    
        xe3 = [coord(cont(i,1),1)-t/2 coord(cont(i,1),1)];
        ye3 = [coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)];
        plot(xe3,ye3,'k','LineWidth',1.5);
        
        x_map_color = [coord(cont(i,1),1) coord(cont(i,1),1)+t/2 coord(cont(i,1),1)-t/2];
        y_map_color = [coord(cont(i,1),2) coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)-t/2*sqrt(3) ];
        fill(x_map_color,y_map_color,'k')
    end
end

% %% PLOTANDO FORCAS %%
% 
% for i=1:size(loads,1)
%     tt=abs(loads(i,3))/max(abs(loads(:,3)))*t;
%     
% if loads(i,2)==1
%        
%         if loads(i,3)<0
%             xe1=[coord(loads(i,1),1) coord(loads(i,1),1)-3*tt+0.6*tt];
%             ye1=[coord(loads(i,1),2) coord(loads(i,1),2)];
%             plot(xe1,ye1,'k','LineWidth',1.5);
%            
%             xe2=[coord(loads(i,1),1)-3*tt coord(loads(i,1),1)-3*tt+0.6*tt];
%             ye2=[coord(loads(i,1),2) coord(loads(i,1),2)+0.2*sqrt(3)*tt];
%             plot(xe2,ye2,'k','LineWidth',1.5); 
%            
%             xe3=[coord(loads(i,1),1)-3*tt coord(loads(i,1),1)-3*tt+0.6*tt];
%             ye3=[coord(loads(i,1),2) coord(loads(i,1),2)-0.2*sqrt(3)*tt];
%             plot(xe3,ye3,'k','LineWidth',1.5);
%            
%             xe4=[coord(loads(i,1),1)-3*tt+0.6*tt coord(loads(i,1),1)-3*tt+0.6*tt];
%             ye4=[coord(loads(i,1),2)+0.2*sqrt(3)*tt coord(loads(i,1),2)-0.2*sqrt(3)*tt];
%             plot(xe4,ye4,'k','LineWidth',1.5);
%            
%             text(coord(loads(i,1),1)-3*tt-0.6*tt,coord(loads(i,1),2),...
%                 strcat(num2str(abs(loads(i,3))),' N'),...
%                 'HorizontalAlignment','right','VerticalAlignment',...
%                 'middle','FontSize',12)
%         end
%        
%         if loads(i,3)>0
%             xe1=[coord(loads(i,1),1) coord(loads(i,1),1)+3*tt-0.6*tt];
%             ye1=[coord(loads(i,1),2) coord(loads(i,1),2)];
%             plot(xe1,ye1,'k','LineWidth',1.5);
%            
%             xe2=[coord(loads(i,1),1)+3*tt coord(loads(i,1),1)+3*tt-0.6*tt];
%             ye2=[coord(loads(i,1),2) coord(loads(i,1),2)+0.2*sqrt(3)*tt];
%             plot(xe2,ye2,'k','LineWidth',1.5); 
%            
%             xe3=[coord(loads(i,1),1)+3*tt coord(loads(i,1),1)+3*tt-0.6*tt];
%             ye3=[coord(loads(i,1),2) coord(loads(i,1),2)-0.2*sqrt(3)*tt];
%             plot(xe3,ye3,'k','LineWidth',1.5);
%            
%             xe4=[coord(loads(i,1),1)+3*tt-0.6*tt coord(loads(i,1),1)+3*tt-0.6*tt];
%             ye4=[coord(loads(i,1),2)+0.2*sqrt(3)*tt coord(loads(i,1),2)-0.2*sqrt(3)*tt];
%             plot(xe4,ye4,'k','LineWidth',1.5);
%            
%             text(coord(loads(i,1),1)+3*tt+0.6*tt,coord(loads(i,1),2),...
%                 strcat(num2str(abs(loads(i,3))),' N'),...
%                 'HorizontalAlignment','left','VerticalAlignment',...
%                 'middle','FontSize',12)
%         end
% end
%      
%     if loads(i,2)==2
%         
%         if loads(i,3)<0
%             xe1=[coord(loads(i,1),1) coord(loads(i,1),1)];
%             ye1=[coord(loads(i,1),2) coord(loads(i,1),2)-3*tt+0.6*tt];
%             plot(xe1,ye1,'k','LineWidth',1.5);
%             
%             xe2=[coord(loads(i,1),1) coord(loads(i,1),1)+0.2*sqrt(3)*tt ];
%             ye2=[coord(loads(i,1),2)-3*tt coord(loads(i,1),2)-3*tt+0.6*tt];
%             plot(xe2,ye2,'k','LineWidth',1.5);  
%             
%             xe3=[coord(loads(i,1),1) coord(loads(i,1),1)-0.2*sqrt(3)*tt];
%             ye3=[coord(loads(i,1),2)-3*tt coord(loads(i,1),2)-3*tt+0.6*tt];
%             plot(xe3,ye3,'k','LineWidth',1.5);
%             
%             xe4=[coord(loads(i,1),1)-0.2*sqrt(3)*tt coord(loads(i,1),1)+0.2*sqrt(3)*tt];
%             ye4=[coord(loads(i,1),2)-3*tt+0.6*tt coord(loads(i,1),2)-3*tt+0.6*tt];
%             plot(xe4,ye4,'k','LineWidth',1.5);
%             
%             text(coord(loads(i,1),1),coord(loads(i,1),2)-3*tt,strcat(num2str(abs(loads(i,3))),' N'),'HorizontalAlignment','center',...
%        'VerticalAlignment','top','FontSize',12)
%         end
%         
%         if loads(i,3)>0
%             xe1=[coord(loads(i,1),1) coord(loads(i,1),1)];
%             ye1=[coord(loads(i,1),2) coord(loads(i,1),2)+3*tt-0.6*tt];
%             plot(xe1,ye1,'k','LineWidth',1.5);
%             
%             xe2=[coord(loads(i,1),1) coord(loads(i,1),1)+0.2*sqrt(3)*tt ];
%             ye2=[coord(loads(i,1),2)+3*tt coord(loads(i,1),2)+3*tt-0.6*tt];
%             plot(xe2,ye2,'k','LineWidth',1.5);  
%             
%             xe3=[coord(loads(i,1),1) coord(loads(i,1),1)-0.2*sqrt(3)*tt];
%             ye3=[coord(loads(i,1),2)+3*tt coord(loads(i,1),2)+3*tt-0.6*tt];
%             plot(xe3,ye3,'k','LineWidth',1.5);
%             
%             xe4=[coord(loads(i,1),1)-0.2*sqrt(3)*tt coord(loads(i,1),1)+0.2*sqrt(3)*tt];
%             ye4=[coord(loads(i,1),2)+3*tt-0.6*tt coord(loads(i,1),2)+3*tt-0.6*tt];
%             plot(xe4,ye4,'k','LineWidth',1.5);
%             
%             text(coord(loads(i,1),1),coord(loads(i,1),2)+3*tt,...
%                 strcat(num2str(abs(loads(i,3))),' N'),'HorizontalAlignment','center',...
%        'VerticalAlignment','bottom','FontSize',12)
%         end
%         
%     end
%     
% end

%% PLOTANDO NUMERO DE ELEMENTOS %%

for i = 1:nel;
   text((coord(inci(i,4),1)+coord(inci(i,5),1))/2,...
        (coord(inci(i,4),2)+coord(inci(i,5),2))/2,num2str(i),...
        'EdgeColor','black','HorizontalAlignment','center',...
        'BackgroundColor',[.9 .9 .9],'FontSize',8);
end

%% PLOTANDO NUMERO DE NOS %%

for i = 1:nnos;
   text(coord(i,1),coord(i,2),num2str(i),'HorizontalAlignment',...
       'center','VerticalAlignment','bottom','FontSize',15);
end
axis equal;

%% PLOTANDO TRELICA DEFORMADA %%

figure(2)

gplot(A,coord_r,'--b');
axis(limits);

hold on;
for i = 1:nel

    no1 = inci(i,4); no2 = inci(i,5);

    xe1 = [ coordX(no1,1), coordX(no2,1)];
    ye1 = [ coordX(no1,2), coordX(no2,2)];  
    
    if i == imax
        plot(xe1,ye1,'-r','LineWidth',4.0*x(i)/max(x));
    else
        plot(xe1,ye1,'-k','LineWidth',4.0*x(i)/max(x));
    end     
end

for i = 1:nnos
    hold on;
    plot(coordX(i,1),coordX(i,2),'ko','LineWidth',1.5)
end

coord = coordX;
t = 0.05*max(Lx,Ly);
for i = 1:size(cont,1)
    if cont(i,2) == 1
        xe1 = [coord(cont(i,1),1) coord(cont(i,1),1)+t/2*sqrt(3)];
        ye1 = [coord(cont(i,1),2) coord(cont(i,1),2)+t/2];
        plot(xe1,ye1,'k','LineWidth',1.5);
    
        xe2 = [coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)+t/2*sqrt(3)];
        ye2 = [coord(cont(i,1),2)+t/2 coord(cont(i,1),2)-t/2];
        plot(xe2,ye2,'k','LineWidth',1.5); 
    
        xe3 = [coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)];
        ye3 = [coord(cont(i,1),2)-t/2 coord(cont(i,1),2)];
        plot(xe3,ye3,'k','LineWidth',1.5);
        
        x_map_color = [coord(cont(i,1),1) coord(cont(i,1),1)+t/2*sqrt(3) coord(cont(i,1),1)+t/2*sqrt(3)];
        y_map_color = [coord(cont(i,1),2) coord(cont(i,1),2)+t/2 coord(cont(i,1),2)-t/2 ];
        fill(x_map_color,y_map_color,'k')
    end
    if cont(i,2) == 2
        xe1 = [coord(cont(i,1),1) coord(cont(i,1),1)+t/2];
        ye1 = [coord(cont(i,1),2) coord(cont(i,1),2)-t/2*sqrt(3)];
        plot(xe1,ye1,'k','LineWidth',1.5);
    
        xe2 = [coord(cont(i,1),1)+t/2 coord(cont(i,1),1)-t/2];
        ye2 = [coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)-t/2*sqrt(3)];
        plot(xe2,ye2,'k','LineWidth',1.5); 
    
        xe3 = [coord(cont(i,1),1)-t/2 coord(cont(i,1),1)];
        ye3 = [coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)];
        plot(xe3,ye3,'k','LineWidth',1.5);
        
        x_map_color = [coord(cont(i,1),1) coord(cont(i,1),1)+t/2 coord(cont(i,1),1)-t/2];
        y_map_color = [coord(cont(i,1),2) coord(cont(i,1),2)-t/2*sqrt(3) coord(cont(i,1),2)-t/2*sqrt(3) ];
        fill(x_map_color,y_map_color,'k')
    end
end
axis equal;
end