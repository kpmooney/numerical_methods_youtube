import numpy as np

from assimulo.solvers import CVode
from assimulo.problem import Explicit_Problem
from assimulo.exception import TerminateSimulation

import matplotlib.pyplot as plt

#  Define out system of equations.  This is the same as in Scipy
def no_drag(t, X):
    Xprime = np.zeros(4)

    Xprime[0] = X[1]
    Xprime[1] = 0
    Xprime[2] = X[3]
    Xprime[3] = -9.8

    return(Xprime)

#  Define out events function.  This is essentially the same as in Scipy
def events(t, X, sw):
    res = np.zeros( X.shape )
    res[2] = X[2] -0

    return res

#  End integration on event detection
def handle_event(solver, event_info):
    raise TerminateSimulation



m = 0.145

#  Initial conditions.  The vector X0 is passed into the solver
v0 = 45
theta = 30; theta = np.radians(theta)
X0 = np.array( [ 0, v0 * np.cos(theta), 1, v0 * np.sin(theta) ] )

#  Time at start of simulation
t0 = 0.0

#  Create a model object with our equations and initial conditions
model = Explicit_Problem(no_drag, X0, t0)
 
#  Bind event functions to model
model.state_events = events
model.handle_event = handle_event

#  Create simulation object
sim = CVode(model)

#  Run simulation
t, X = sim.simulate(5, 100)

print(X.shape)

#print(t[-1], X[-1, :])

#  Plot results
plt.plot(X[:, 0], X[:, 2], '.')
plt.show()

