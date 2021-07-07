import numpy as np

import matplotlib.pyplot as plt

samples = 1000          #  Number of runs used in the simulation

days = 38               #  Number of trading days to our target date
dt = 1.0                #  Time steps of one day
r = 0.02 / 252.0                #  Risk-free rate
sigma = 0.269 / np.sqrt(252.0)  #  Volatility

#  Create a matrix of random numers sampled from the standard normal
#  distribution.  Then create a matrix of fractional price changes.  The
#  form we are using is each row of the matrix is one simulation, each
#  column is a day.
epsilon = np.random.normal( size = (samples, days) )
ds_s = r * dt + sigma * epsilon

#  Initialize a matrix to hold out final price data.  We add an additional
#  column for the initial price.
prices = np.zeros( (epsilon.shape[0], epsilon.shape[1] + 1) )

#  Set the initial price
prices[:, 0] = 196.8

#  Use the fractional price change matrix to figure out the price changes.
#  This loops through each column filling in all rows in that column at the
#  same time.
for i in range(days):
    prices[:, i+1] = prices[:, i] + ds_s[:, i] * prices[:, i]

#  Find the unique indices which meet our touch criteria.
ind = np.where( prices >= 215.0)
U = np.unique( ind[0] )

#  Work out and print the probability of a touch
print( float(len(U)) / float(samples) )

