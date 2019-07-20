import numpy as np
from scipy.integrate import solve_ivp

import matplotlib.pyplot as plt

#  Function to be integrated in the form of yprime = (f(t, y)
def equations(t, y):

    #  Constants
    m = 70
    R0 = 6370000
    H = 8000

    #  Calculate position-depenent gravity and height-dependent drag
    #  coefficient.
    g = 9.81 / (1 + y[0] / R0)**2
    c2 = 0.5 * np.exp(-y[0] / H)

    #  Drag force
    F_drag = -c2 * y[1] * np.abs(y[1])

    #  dy/dt = V
    yprime  = y[1]

    #  Acceleration, dV/dt = Force / mass
    vprime = (-m*g + F_drag) / m

    #  Return values
    return [yprime, vprime]

def events(t, y):
    return y[0] - 0

events.terminal = True

#  Set up initial conditions
y0 = [32000, 0]

#  The variable tspan has the start and end times of the inegration which
#  teval is a vector of time points for the solution to be evaulated at.
tspan = (0, 1200)
teval = np.linspace(tspan[0], tspan[1], 1000)

#  Call the solver.
sol = solve_ivp(equations, tspan, y0, t_eval = teval, events = events)

#  Extract the time and position/velocty vector from sol
t = sol.t
y = sol.y

# Print the time to impact.  This will be an empty vector if no event was
# detected.
print('Time to impact = ', sol.t_events[-1]);


#  Plot the results
plt.subplot(1, 2, 1); plt.plot(t, y[0, :], 'k')
plt.xlabel('Time (s)'); plt.ylabel('Altitude (m)');
plt.subplot(1, 2, 2); plt.plot(t, y[1, :], 'k')
plt.xlabel('Time (s)'); plt.ylabel('Velocity (m/s)');
plt.show()
