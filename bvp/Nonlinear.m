classdef Nonlinear < handle

properties

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

    function obj = Nonlinear()
        
        clc; close all;
        N = 10000;
        x = linspace(0, pi / 2, N);
        Delta = diff(x); Delta = Delta(1);
        obj.Delta = Delta;
        
        y = [ones( length(x), 1 ), -2 * ones(length(x), 1), ...
            ones(length(x), 1)];

        obj.D2 = spdiags(y, [-1, 0, 1], length(x), length(x));
        obj.D2 = obj.D2 / Delta^2;
        obj.E = eye(length(x));
        
        obj.known = zeros(length(x), 1);
        obj.known(1) = 1;
        obj.known(end) = 0;
        
%        options = optimoptions('fsolve','Display','none');
        options = optimoptions('fsolve','Display','none', ...
            'SpecifyObjectiveGradient',true);

        tic;
        sol = fsolve(@obj.equations2, 0.5 * ones(length(x), 1), options);
        toc;
        plot(x, sol);
        obj.sol = sol;

    end

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
