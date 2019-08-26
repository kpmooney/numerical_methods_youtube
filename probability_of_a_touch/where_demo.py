import numpy as np

#  Create a test matrix and print it to the screen
a = np.array( [ [ 1, 2, 3, 4, 5], [5, 5, 1, 9, 4], [1, 1, 1, 1, 10] ] )
print(a)
print('\n')

#  The find matrix indices where the entry is greater than or equal to
#  five.  Print these to the screen
ind = np.where( a >= 5 )
print(ind)

#  Print row indices where a >=5
print(ind[0])

#  Filter the results through the unique command to remove duplicates
print( np.unique( ind[0] ) )
