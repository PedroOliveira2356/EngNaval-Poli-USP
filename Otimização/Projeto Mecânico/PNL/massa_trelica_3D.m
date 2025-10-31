function wval = massa_trelica_3D(x)

global coord inci tmat

nel = length(x);

wval = 0;
for i = 1:nel

    noi = inci(i,4); 
    noj = inci(i,5);
 
    x1 = coord(noi,1); x2 = coord(noj,1);
    y1 = coord(noi,2); y2 = coord(noj,2);
    z1 = coord(noi,3); z2 = coord(noj,3);
    
    Le = sqrt( (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2 );
   
    A = pi*x(i)^2/4;
    
    rho = tmat(3,inci(i,3));
    
    wval = wval + rho*A*Le;
end


end