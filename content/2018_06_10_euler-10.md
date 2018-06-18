title: Problem 10 - Summation of Primes
date: 10 June 2018
category: euler
tags: primes
slug: euler/10
problem: 10
summary: My solution to problem 10 of Project Euler.

# Problem Statement

The sum of all primes below 10 is $2+3+5+7 = 17$.
Find the sum of all primes at most $N$.

# My Algorithm

We use a Sieve of Eratosthenes to compute the primes up to the maximum possible value of $N$.
We then construct a prefix sum array in $O(\frac{N}{\log N})$ time.
Using a binary search, we find the index of largest prime less than $N$ in $O(\log N - \log \log N)$ time.
In $O(1)$ time, we look up the corresponding partial sum of prime numbers.
Our solution has time complexity $O(n\log\log n + \frac{n}{\log n} + T\log n)$, where $T$ is the number of queries.