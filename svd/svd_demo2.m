clear all; close all; clc;

image = imread('IMG_20180805_190645.jpg');
image = rgb2gray(image);
image = im2double(image);

imshow(image)

[U, S, V] = svd(image);


N = 10;
M = U(:, 1:N) * S(1:N, 1:N) * V(:, 1:N)';

figure();
imshow(M);


