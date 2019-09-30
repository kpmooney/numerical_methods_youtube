import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x) - 5 * x

def dfdx(x):
    return np.exp(x) - 5

#  Tolerances
tol = 1e-3
epsilon = 1

#  Variables to log and manage number of iterations
count = 0
max_iter = 1000

#  Initial guess
R = -2

while epsilon > tol:
    #  Count how many iterations and make sure while loop doesn't run away
    count += 1
    if count >= max_iter:
        print('Breaking on count')
        break;

    #  Log the value previously calculated to computer percent change
    #  between iterations
    orig_R = R

    function_value = f(R)

    #  Calculate derivative
    df = dfdx(R)

    #  Update for value of our root
    R = -function_value / df + R

    #  Check the percent change between current and last iteration
    epsilon = abs( (R - orig_R) / orig_R )

print(R)

x = np.linspace(-5, 5);
y = np.exp(x) - 5 * x

plt.plot(x, y, 'b', label=r'$e^x - 5x$')
plt.plot(R, f(R), 'bo')
plt.grid(True)
plt.ylim([-10, 20])
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper center')
plt.show()


