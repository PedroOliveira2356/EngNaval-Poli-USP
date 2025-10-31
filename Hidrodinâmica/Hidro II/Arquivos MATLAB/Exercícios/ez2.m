clear all; close all; clc;
figure; hold on
ezplot("2*y-(2*1^2*y)/(x^2+y^2)-log(x^2+y^2)", [-2 2 -2 2]);
for c=1:3
    Exp1 = "2*y-(2*1^2*y)/(x^2+y^2)-log(x^2+y^2)+" + (c/2);
    Exp2 = "2*y-(2*1^2*y)/(x^2+y^2)-log(x^2+y^2)-" + (c/2);
    ezplot(Exp1, [-2 2 -2 2]);
    ezplot(Exp2, [-2 2 -2 2]);
end