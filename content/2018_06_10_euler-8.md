title: Problem 8 - Largest Product in a Series
date: 10 June 2018
category: euler
tags: brute-force
slug: euler/8
problem: 8
summary: My solution to problem 8 of Project Euler.

# Problem Statement

Find the greatest product of $K$ consecutive digits in the given $N$ digit number.

# My Algorithm

We use a brute force solution.
There are $N-K+1$ possible $K$-length substrings of a string of length $N$.
We convert the given number to a string, find the substrings, and multiply the digits in them.
We then find the maximal product.
This is easily done with time complexity $O(K(N-K+1))$.