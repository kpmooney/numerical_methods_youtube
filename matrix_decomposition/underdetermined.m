function underdetermined()
clear all; clc; close all;

%  Set a constant seed
rng(2);

%  Create our matrices
A = rand( 3, 5 );
b = rand( 3, 1 );

%  Solve the system
x2 = pinv(A) * b

    %  Define a function to minimze
    function N = f(x)
        N = norm(x);
    end

%  Minimize the function with the constraint that Ax = b
x = fmincon(@f, zeros(5,1), [], [], A, b)

%  Are these essentially the same?
abs(x2 - x) <= 1e-6

end
