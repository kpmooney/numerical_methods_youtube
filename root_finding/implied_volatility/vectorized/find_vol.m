function find_vol

clear all; clc; close all;

%  Data file format S_call, K_call, r_call, t_call, bid_call, ask_call
data = load('option_data.dat');
data = data';

%  Extract data
S     = data(:,1);
K     = data(:,2);
r     = data(:,3);
t     = data(:,4);
bid   = data(:,5);
ask   = data(:,6);

%  Call our solution function and plot the results
x = wrapper(S, K, r, t, ask);
plot(x)

function [C, d1, d2] = call_price(sigma, S, K, r, t)

    d1 = 1 ./ (sigma .* sqrt(t)) .* ( log(S./K) + (r + sigma.^2/2) .* t);
    d2 = d1 - sigma .* sqrt(t);

    C = normcdf(d1) .* S - normcdf(d2) .* K .* exp(-r .* t);
end


function x = wrapper(S, K, r, t, price)

    %  Our initial guess
    x0 = 3 * ones(size(S));

    %  Call the fsolve root finder
    options = optimoptions(@fsolve, 'SpecifyObjectiveGradient', true, ...
        'MaxIterations', 10000);
    x = fsolve(@obj, x0, options);

    %  Our objective function
    function [f, J] = obj(sigma)
        [C, d1, d2] = call_price(sigma, S, K, r, t);
        vega = S .* normpdf(d1) .* sqrt(t);
        J = spdiags(vega, 0, length(vega), length(vega));
        f =  C - price;
    end

end


end
