import numpy as np

#  Number of random points generated
N = 1000000

#  Generate an N x 2 matrix of random numbers all bewteen zero and one
points = np.random.rand( N, 2 )

#  Figure out the distance from the origin to each point:  This is the same
#  as sqrt(x^2 + y^2)
norms =np.linalg.norm(points, axis = 1)

#  Create a boolean vector to determine if each point is in or out of the
#  circle
inside_circle = norms <= 1

#  Calculate the number if points in the circle.  sum on a bololean vector
#  treatss True as one and False as zero.
number_in_circle = float( sum(inside_circle) )

#  Print our estimate of pi
print( 4 * number_in_circle / float(N) )
