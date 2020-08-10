iclear all; clc; close all;

X = [ [1 2 3 4 5]; [6 7 8 9 10]; [11 12 13 14 15]]

[U, S, V] = svd(X)

U * S *V'

