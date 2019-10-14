import numpy as np
from scipy.optimize import minimize

import matplotlib.pyplot as plt

def specific_heat(p, theta):
    #  Etract individual parameters from p vector
    A     = p[0]
    alpha = p[1]
    B     = p[2]
    D     = p[3]

    #  Return specific heat
    return (A/alpha) * np.power(theta, -alpha) * (1.0 +
        D * np.power(theta, 0.5)) + B

def objective(q, theta_warm, theta_cold, C_warm_exp, C_cold_exp):
    #  Extract the parameters from the array q and calculate the specific
    #  heat on the warm side
    #  Format is (A, APrime, alpha, B, D, Dprime)
    p = [q[0], q[2], q[3], q[4]]
    C_warm = specific_heat(p, theta_warm)

    #  Extract the parameters from the array q and calculate the specific
    #  heat on the cold side
    p = [q[1], q[2], q[3], q[5]]
    C_cold = specific_heat(p, theta_cold)

    error_warm_sq = np.square(C_warm - C_warm_exp)
    error_cold_sq = np.square(C_cold - C_cold_exp)

    res = np.sum(error_warm_sq) + np.sum(error_cold_sq)
    return res



#  Import raw data
raw_cold_data = np.loadtxt('cold_data.txt')
raw_warm_data = np.loadtxt('warm_data.txt')

#  The temperature and specific heat are in the first and seconds columns,
#  respectively.  We pull them into their own variables for simplicity's
#  sake
theta_warm = raw_warm_data[0, :]
C_warm     = raw_warm_data[1, :]
theta_cold = raw_cold_data[0, :]
C_cold     = raw_cold_data[1, :]

#  Format is (A, APrime, alpha, B, D, Dprime)
q = [7.0, 10.0, -0.021, 375.0, -0.01, -0.01]

#  Call the minimization routine. We are using the Powell method to avoid
#  issues with the gradient being a problem at alpha = 0.
results = minimize(objective, q, args=(theta_warm, theta_cold, 
    C_warm, C_cold), method='Powell')

#  Print out the results object.
print(results)

# Extract the parameters from the results object.
A      =  results.x[0]
Aprime =  results.x[1]
alpha  =  results.x[2]
B      =  results.x[3]
D      =  results.x[4]
Dprime =  results.x[5]

#  Calculate the specific heat using our fitted values.
C_warm_fit = specific_heat( [A, alpha, B, D], theta_warm)
C_cold_fit = specific_heat( [Aprime, alpha, B, Dprime], theta_cold)

#  Plot the results on a semilog plot.
plt.semilogx(theta_warm, C_warm, 'or', label = r'$\theta > \theta_\lambda$')
plt.semilogx(theta_cold, C_cold, 'ob', label = r'$\theta < \theta_\lambda$')
plt.semilogx(theta_warm, C_warm_fit, 'y')
plt.semilogx(theta_cold, C_cold_fit, 'y')
plt.xlabel(r'$\theta$')
plt.ylabel(r'$C_{p\phi}\quad \left(\frac{\mathrm{J}}{\mathrm{mol\quad K}}\right)$')
plt.legend()
plt.show()
