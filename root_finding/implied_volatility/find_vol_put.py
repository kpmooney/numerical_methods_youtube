from math import sqrt, exp, log, pi
from scipy.stats import norm

#   Function to calculate the values of 21 and d2 as well as the call
#   price.  To extend to puts, one could just add a function that
#   calculates the put price, or combine calls and puts into a single
#   function that takes an argument specifying which type of contract one
#   is dealing with.
def d(sigma, S, K, r, t):
    d1 = 1 / (sigma * sqrt(t)) * ( log(S/K) + (r + sigma**2/2) * t)
    d2 = d1 - sigma * sqrt(t)
    return d1, d2

def call_price(sigma, S, K, r, t, d1, d2):
    C = norm.cdf(d1) * S - norm.cdf(d2) * K * exp(-r * t)
    return C


def put_price(sigma, S, K, r, t, d1, d2):
    P = -norm.cdf(-d1) * S + norm.cdf(-d2) * K * exp(-r * t)
    return P


#  Option parameters
S = 100.0
K = 95.0
t = 30.0 / 365.0
r = 0.01
P0 =2.30


#  Tolerances
tol = 1e-3
epsilon = 1

#  Variables to log and manage number of iterations
count = 0
max_iter = 1000

#  We need to provide an initial guess for the root of our function
vol = 0.50

while epsilon > tol:
    #  Count how many iterations and make sure while loop doesn't run away
    count += 1
    if count >= max_iter:
        print('Breaking on count')
        break;

    #  Log the value previously calculated to computer percent change
    #  between iterations
    orig_vol = vol

    #  Calculate the vale of the call price
    d1, d2 = d(vol, S, K, r, t)
    function_value = put_price(vol, S, K, r, t, d1, d2) - P0

    #  Calculate vega, the derivative of the price with respect to
    #  volatility
    vega = S * norm.pdf(d1) * sqrt(t)

    #  Update for value of the volatility
    vol = -function_value / vega + vol

    #  Check the percent change between current and last iteration
    epsilon = abs( (vol - orig_vol) / orig_vol )

#  Print out the results
print('Sigma = ', vol)
print('Code took ', count, ' iterations')

