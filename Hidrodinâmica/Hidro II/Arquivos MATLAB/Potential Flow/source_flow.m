function P = source_flow(P,X,Y,x0,y0,q)

r = sqrt((X-x0).^2 + ((Y-y0).^2));

P = P + q/(2*pi) * log(r);

end

