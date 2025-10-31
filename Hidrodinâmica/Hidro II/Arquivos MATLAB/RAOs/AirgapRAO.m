clc
close all
clear all

% load('RAOsFOWTC.mat')
load('RAOsEvenKeel.mat')
% load('RAOsHeelTrim.mat')


P = [70,0,15.5]; % ponto considerado a origem no centro da torre e na linha de agua
CM = -11.72; % posicao do CM em relaca á origem
A = 1;
for i = 1:length(vetor_Ti)
    for j = 1:length(vetor_ai)
        
        % Surge
		R(:,:,1) = A.*[cosd(raophat(i,j,1)) sind(raophat(i,j,1))]'*P.*[raoampt(i,j,1), 0, 0];
			
		% Sway
		R(:,:,2) = A.*[cosd(raophat(i,j,2)) sind(raophat(i,j,2))]'*[0, raoampt(i,j,2), 0];
			
		% Heave
        R(:,:,3) = A.*[cosd(raophat(i,j,3)) sind(raophat(i,j,3))]'*[ 0, 0,raoampt(i,j,3)];
        
         % Roll
        cr = cosd(raoampt(i,j,4));
        sr = sind(raoampt(i,j,4));
		R(:,:,4) = A.*[cosd(raophat(i,j,4)) sind(raophat(i,j,4))]'.*([1 0 0; 0 cr -sr; 0 sr cr]*(P+[0,0,-CM])'+[0,0,CM]'-P')';
        
        % Pitch       
	    cp = cosd(raoampt(i,j,5));
	    sp = sind(raoampt(i,j,5));
		R(:,:,5) = A.*[cosd(raophat(i,j,5)) sind(raophat(i,j,5))]'.*([cp 0 sp; 0 1 0; -sp 0 cp]*(P+[0,0,-CM])'+[0,0,CM]'-P')';
        
        % Yaw        
		cy = cosd(raoampt(i,j,6));
		sy = sind(raoampt(i,j,6));
		R(:,:,6) = A.*[cosd(raophat(i,j,6)) sind(raophat(i,j,6))]'.*([cy -sy 0; sy cy 0; 0 0 1]*(P+[0,0,-CM])'+[0,0,CM]'-P')';
		
        
        % Motion = rotation + linear 
        Airgap(i,j,:) = [0,0,A]- sum(sum(R,3).^2,1).^0.5 ;
       
    end
end

surf(vetor_ai,vetor_Ti,Airgap(:,:,3))
xlabel('Âng. incidência')
ylabel('Período')
zlabel('Airgap - EvenKell')
% zlabel('Airgap - HeelTrim')

