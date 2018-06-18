‐‐‐
title: Problem 27 - Quadratic Primes
date: 13 June 2018
category: euler
tags: brute-force
slug: euler/27
problem: 27
summary: My solution to problem 27 of Project Euler.
‐‐‐

# Problem Statement

Euler published the remarkable quadratic equation
\begin{equation*}
	n^2 + 41n + 41.
\end{equation*}
It turns out that the formula will produce 40 primes for the consecutive integer values $0 \le n \le 39$.
However, when $n = 40$, we have $40^2 + 40 + 41 = 41(40+1) + 41$, which is divisiblye by 41, and certainly when $n = 41$, the expression $41^2 + 41 + 41$ is clearly divisible by 41.

The incredible formula $n^2 - 79n + 1601$ produces 80 primes for the consecutive values $0 \le n \le 79$.

Considering quadratics of the form
\begin{equation*}
	n^2 + an + b, \quad |a|,|b| \le N,
\end{equation*}
find the coefficients $a,b$ for the quadratic expression that produces the maximum number of primes with consecutive values of $n$, starting with $n = 0$.

# My Algorithm

A naive brute force search over all $-N \le a,b \le N$ is too slow.
We make two observations that exclude many cases.
First, the expression $n^2 + an + b$ is equal to $b$ when $n = 0$.
Thus $b$ must be prime.
Second, when $n = 1$, we have $1 + a + b$.
Above 2, $b$ is odd.
So $a$ must also be odd; otherwise, the expression is an even number greater than 2, which is not prime.

We need two things to proceed: a list of primes under $N$ and a way to check if a given $n$ is prime.
For the first, we use a Sieve of Eratosthenes, and for the second, we use trial division up to $\sqrt{n}$.
We iterate through odd $-N \le a \le N$, which takes $N$ steps, and prime $-N \le b N$, which takes about $\frac{N}{\log N}$.
Then, we compute the expression $n^2 + an + b$ until it is not prime; we do this up to $N$ times, with time complexity $\sqrt{N}$ each time.
Including the sieve, our solution has time complexity $O\left(N\cdot\frac{N}{\log N}\cdot N\sqrt{N} + \sqrt{N}\log\log N\right) \in O\left(\frac{N^3\sqrt{N}}{\log N}\right)$.
