import numpy as np
from math import sqrt
from time import time

#  Number of points to us in the approximation
N = 10000000

start = time()
#  Create a matrix of N paris of numbers
points = np.random.rand( N, 2 )

#  Calculate the norm of each row
norms = np.linalg.norm(points, axis = 1)

#  Determine if each point is in the circle
inside_circle = norms <= 1

#  Count the number in the circle
number_in_circle =  float( np.sum(inside_circle) )
end = time()

#  Print the estimate of pi and the run time
print( 4 * number_in_circle / float(N) )
print('Time = ', end - start)

#  Set number in circle to zero
number_in_circle = 0

start = time()

#  begin loop
for i in range(N):
    #  Calculate random values for our xy-pair
    x = np.random.rand()
    y = np.random.rand()

    #  Calculate norm of resulting vector
    norm = sqrt( x**2 + y**2 )

    # Is this point inside the circle
    inside_circle = norm <= 1

    #  If yes, increment number in circle by one.
    if inside_circle == True:
        number_in_circle += 1

end = time()

#  Print the estimate of pi and the run time
print( 4 * number_in_circle / float(N) )
print('Time = ', end - start)
