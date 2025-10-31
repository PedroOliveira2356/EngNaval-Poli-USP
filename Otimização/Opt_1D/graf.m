function graf(I,X)
    x=[I(1):0.01:I(2)];
    
    for i=1:length(x)
        y(i) = f(x(i));
    end
    
    figure(2)
    plot(x,y)
    title('Curva da função')
end