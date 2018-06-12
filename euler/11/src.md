‐‐‐
title: Problem 11 - Largest Product in a Grid
date: 10 June 2018
category: euler
tags: proof
slug: euler/11
summary: My solution to problem 11 of Project Euler.
‐‐‐

# Problem Statement

In the 20-by-20 grid below, four numbers have been marked in bold.

![A nice friendly matrix.](../../figures/euler-11-matrix.png){ width=95% }

The product of these numbers is $26 \cdot 63 \cdot 78 \cdot 14 = 1788696$.
What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20Ã—20 grid?

# My Algorithm

The important thing in this problem is to be careful of boundary conditions.
We start at the top left corner.
If there are at least three cells to the right, we check the horizontal product.
If there are at least three cells down, we check the vertical product.
If there are at least three cells to the left and three cells down, we check the left diagonal product.
If there are at least three cells to the right and three cells down, we check the right diagonal product.
Checking up, left, left-up, or right-up would be redundant.
We take the maximum of these four values and the existing maximum product and set that to be our new maximum product.
We continue like this over all cells in the grid.
Our final answer is found in $O(n^2)$ time---not surprising for a square grid.