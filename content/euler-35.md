title: Problem 35 - Circular Primes
date: 24 June 2018
category: euler
tags: brute-force
slug: euler/35
problem: 35
summary: My solution to problem 35 of Project Euler.

# Problem Statement

The number 197 is called a circular prime because all rotations of the digits (197,719,917) are prime.
There are thirteen such prime under 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

What is the sum of all circular primes less than $N$?

# My Algorithm

A permutation of a number $n$ cannot be greater than the smallest power of 10 not more than $n$.
This is because it maintains the same number of digits, and such a power of 10 contains one more digit than $n$.
This means that a permutation of $n$ is not more than $10^{\lceil \log_{10} n \rceil}$.
And so we can precompute a list of the primes under $10^{\lceil \log_{10} N_{\text{max}} \rceil}$, which in our case is $10^6$.

Then, we need a way to get all the rotations of a number.
To do this, we can turn the number into a string and repeatedly remove the last character and add it back to the front, saving the new rotation each time.

From here, the problem just consists of spotting some optimizations.
We need not check any primes with digits 0, 2, 4, 5, 6, or 8.
This is because the last digit of one of their rotations will be either even or 5, which means they are divisible by 2 or 5 and so they are not prime.
However, we must include the single-digit primes 2 and 5, which are circular.
After computing the rotations of a prime below $N$ that passes the above tests, we check if all of them are prime; if so, we count the ones that are below $N$.

Our solution has time complexity $O(N_{\text{max}}\log\log N_{\text{max}})$.