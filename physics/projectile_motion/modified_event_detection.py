import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp
from scipy.optimize import minimize

from scipy.interpolate import interp1d

#  Vector format
#   x[0] = x position
#   x[1] = x velocity
#   x[2] = y position
#   x[3] = y velocity

#  For 30 degrees, when does it reach its max height?
#  For 30 degrees, how far does the ball travel in the x-direction?

def no_drag(t, X):
    Xprime = np.zeros(4)

    Xprime[0] = X[1]
    Xprime[1] = 0
    Xprime[2] = X[3]
    Xprime[3] = -9.8

    return(Xprime)

def events(t, X):
    return X[2] - 0

events.terminal = True

#  Calculates the entir trajectory to some specified end time
def calculate_trajectory(t_end):
    m = 0.145               #  mass in kg

    v0 = 45
    theta = 30; theta = np.radians(theta)
    X0 = np.array( [ 0, v0 * np.cos(theta), 1, v0 * np.sin(theta) ] )

    tspan = (0, t_end)
    t_eval = np.linspace(tspan[0], tspan[1], 100)

    sol = solve_ivp(no_drag, tspan, X0, method = 'RK45', t_eval = t_eval,
        events = events)

    t_evt = sol.t_events[0][0]

    sol2 = solve_ivp(no_drag, tspan, X0, method = 'RK45', t_eval = t_eval)
    t  = sol2.t
    x  = sol2.y[0,:]
    vx = sol2.y[1,:]
    y  = sol2.y[2,:]
    vy = sol2.y[3,:]

    #  Use a cubic spline to interpolate too get values at t_evt
    sp_x  = interp1d(t, x, kind = 'cubic')
    sp_vx = interp1d(t, vx, kind = 'cubic')
    sp_y  = interp1d(t, y, kind = 'cubic')
    sp_vy = interp1d(t, vy, kind = 'cubic')

    #  Place data in new array
    new_data = np.array( [
        sp_x(t_evt), 
        sp_vx(t_evt), 
        sp_y(t_evt), 
        sp_vy(t_evt) ] )

    #  The data needs to be explicitly shaped into a column vector
    new_data.shape = (4, 1)

    #  Append the data to our original solution
    sol.t = np.append(sol.t, t_evt)
    sol.y = np.append(sol.y, new_data, 1)


    return sol

#  From Sympu:  R = 180.664729951254
#  From numeric integration with tf = 5 and N = 100
#  Event Time =  [array([4.63585913])]
#  Numerical range =  179.10979941905433
#  Error =  1.554930532199677

sol = calculate_trajectory( 5 )
x = sol.y[0,:]
y = sol.y[2,:]

plt.plot(x, y, '.')
plt.grid(True)
plt.xlabel('Distance (m)')
plt.ylabel('Height (m)')
plt.show()
