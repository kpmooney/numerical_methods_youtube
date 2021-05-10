classdef Nonlinear < handle

properties

    %  Define our class vairables
    x;
    Delta;
    D2;
    E;
    known;
    sol;
    num;
    J;

end %  End of properties

methods

    %  Class constructor
    function obj = Nonlinear()
        
        clc; close all;

        % Set the number of grid points and create our x-values.  We allso
        % calculate the grid spacing in the variable Delta.
        N = 10000;
        x = linspace(0, pi / 2, N);
        Delta = diff(x); Delta = Delta(1);
        obj.Delta = Delta;
        
        %  Create an array defining how our second derivative matrix shall
        %  be built
        y = [ones( length(x), 1 ), -2 * ones(length(x), 1), ...
            ones(length(x), 1)];

        %  Create the sparce matrix and divide though buy Delta^2
        obj.D2 = spdiags(y, [-1, 0, 1], length(x), length(x));
        obj.D2 = obj.D2 / Delta^2;

        %  The matrix that captures the y-variable is just the identity
        obj.E = speye(length(x));
        
        %  Create our vector of known values.
        obj.known = zeros(length(x), 1);
        obj.known(1) = 1;
        obj.known(end) = 0;
        
%       The first options setting does not use the provided Jacobian.  It is
%       calculated numerically using full matrices.  The second options setting
%       uses our sparse Jacobian.  Uncomment whichever option you want to try.
%        optsons = optimoptions('fsolve','Display','none');
        options = optimoptions('fsolve','Display','none', ...
            'SpecifyObjectiveGradient', true);

        %  Solve the nonlinear system and keep track of the time taken.
        tic;
        sol = fsolve(@obj.equations2, 0.5 * ones(length(x), 1), options);
        toc;

        %  Plot the solution
        plot(x, sol, 'k');

        %  Attach the solution to a class variable in case we need access
        %  to it from outside.
        obj.sol = sol;

    end

    %  These are the function which encode our nonlinear equation  I
    %  created two version.  One also returns the Jacobian while the other
    %  does not.
    function res =  equations(obj, y)
        M = obj.D2 * y + obj.Y * y.^3;
        M(1) = y(1) - obj.known(1);
        M(end) = y(end) - obj.known(end);

        res = M - obj.known;
        res(1) = y(1) - obj.known(1);
        res(end) = y(end) - obj.known(end);
    end

    function [res, J] =  equations2(obj, y)
        M = obj.D2 * y + obj.E * y.^3;
        M(1) = y(1) - obj.known(1);
        M(end) = y(end) - obj.known(end);

        res = M - obj.known;
        res(1) = y(1) - obj.known(1);
        res(end) = y(end) - obj.known(end);

        J = obj.D2 + obj.E * 3 .* y.^2;
        J(end, end) = 1;
        J(end, end-1) = 0;
        J(1,1) = 1;
        J(1,2) = 0;
    end

end

end
