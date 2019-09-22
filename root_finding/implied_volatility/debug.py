from math import sqrt, exp, log, pi
from scipy.stats import norm

import numpy as np
import matplotlib.pyplot as plt

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


#  Option parameters
S = 100.0
K = 90.0
t = 30.0 / 365.0
r = 0.01
C0 =10.30

sigma = np.linspace(0, 1)
d1, d2 =  d(sigma, S, K, r, t)
C = call_price(sigma, S, K, r, t, d1, d2)

plt.plot(sigma, C - C0)
plt.show()


