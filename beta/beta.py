#  Import Numpy and the stats module of SciPy which contrains the linear
#  regression function
import numpy as np
from scipy import stats

#  We're using Pandas to import the raw data.  Pandas also has a built-in
#  function to calculate percent changes which we will also use
import pandas as pd

# Just in case we want to plot something for diagnostic purpoases
import matplotlib.pyplot as plt


#  Import AAPL and SPX data each into their own data frame
AAPL_frame = pd.read_csv('AAPL.csv')
SPX_frame = pd.read_csv('SPX.csv')

#  Calculate the daily percent change and return it as a Numpy array
AAPL_pct = AAPL_frame['Adj Close'].pct_change().values
SPX_pct = SPX_frame['Adj Close'].pct_change().values

#  Delete the first element of each array which is NaN.  The fitting
#  routine can't handle missing values.
AAPL_pct = np.delete(AAPL_pct, 0)
SPX_pct = np.delete(SPX_pct, 0)

#  Do the fit and print the slope (whuch is out beta value) to the screen.
slope, intercept, r, p, std_err  = stats.linregress(SPX_pct,AAPL_pct)
print('Beta = ', slope)

#  Create data needed to plot a the fit.  x starts and the min value of the
#  SPX data and goes to the max SPX value
x = np.linspace(np.amin(SPX_pct), np.amax(SPX_pct))
y = slope * x + intercept

#  Plot it!
plt.plot(SPX_pct, AAPL_pct, 'b.', alpha = 0.2)
plt.plot(x, y, 'k')
plt.grid(True)
plt.show()
