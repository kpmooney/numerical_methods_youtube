clear all; close all; clc;

image = imread('IMG_20180805_190645.jpg');
image = rgb2gray(image);
image = im2double(image);

imshow(image)

[U, S, V] = svds(image, 10);


M = U * S * V';

figure();
imshow(M);



