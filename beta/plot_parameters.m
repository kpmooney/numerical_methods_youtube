function plot_parameters
    clear all; clc; close all;

    #  oad in raw data
    AAPL = load('AAPL_pct.csv');
    SPX = load('SPX_pct.csv');

    %  Create m and b vecotrs for plotting.  There will be N points used,
    N = 20;
    m = linspace(-500, 500, N);
    b = linspace(-5, 5, N);

    %  Cread the grid needed for the plotting function
    [M, B] = meshgrid(m, b);

    %  Evaluate the error function
    f = error_sum(M, B);

    %  Plot it!
    surf(M, B, f);
    xlabel('m');
    ylabel('b');
    zlabel('Function Value');

    %  Find the values of m and b which minimize the error function and
    %  print the results to the console.
    results = fminunc(@new_error, [0, 0]);
    fprintf('m = %1.6f\n', results(1));
    fprintf('b = %1.6f\n', results(2));

    %  Error function used for plotting
    function res = error_sum(M, B)

        res = zeros( length(m), length(b) );
        for i = 1:length(AAPL)
            y = AAPL(i);
            x = SPX(i);
            e = (y - M * x - B).^2;
            res = res + e;
        end;
    end;

    %  Error function used to find the minimum.
    function res = new_error(p)
        res = 0;
        m = p(1);
        b = p(2);
        for i = 1:length(AAPL)
            y = AAPL(i);
            x = SPX(i);
            e = (y - m * x - b)^2;
            res = res + e;
        end;
    end;



end
