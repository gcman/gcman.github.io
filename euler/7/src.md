‐‐‐
title: Problem 7 - 10001st Prime
date: 10 June 2018
category: euler
tags: proof
slug: euler/7
summary: My solution to problem 7 of Project Euler.
‐‐‐

# Problem Statement

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the $N$-th prime number?

# My Algorithm

We use the following identity, which is a consequence of the Prime Number Theorem:
\begin{equation}
	n(\log n + \log \log n - 1) < p_n < n(\log n + \log \log n), n > 5.
\end{equation}
If $n <= 5$, we use a look-up table.
Using a Sieve of Eratosthenes, we generate a list of the primes up to $n(\log n + \log \log n)$, which is guaranteed to contain the $n$-th prime.
Our answer is the $n$-th element of this array.
We do this with time complexity $O(n \log n \log \log (n \log n))$, using $p_n \approx n \log n$.

To optimize the constant factor, we compute the first $N_{\text{max}} = 10^4$ primes and store them in memory, rather than computing the list for each query, which takes too long. 