‐‐‐
title: Problem 1: Multiples of 3 and 5
date: 9 June 2018
category: euler
tags: proof
slug: euler/1
summary: My solution to problem 1 of Project Euler.
‐‐‐

# Problem Statement

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below $n$.

# My Algorithm

For the Project Euler problem, $n = 1000$.

In general, the sum of the natural numbers up to $n$ is the $n$-th *triangular number* (see [here](https://en.wikipedia.org/wiki/Triangular_number)).
Let's call this $T(n)$.
A well known formula for this is
\begin{equation}
	T(n) = \sum_{i=1}^n i = \frac{n(n+1)}{2}
	\label{triangular-num}
\end{equation}

The sum of all multiples of 3 below $n$ looks like this:
\begin{equation}
	1\cdot3 + 2\cdot 3 + 3 \cdot 3 + \ldots + \floor{\frac{n-1}{3}} \cdot 3.
	\label{3-list}
\end{equation}
We can factor 3 out and write \eqref{3-list} as $3T\floor{\frac{n-1}{3}}$, which we know how to find with \eqref{triangular-num}.
We can do the same thing with 5.

But now we've overcounted!
Each multiple of 15 under $n$ has been counted twice: once as a multiple of 3, then again as a multiple of 5.
We can fix this by subtracting the sum of all multiples of 15 under $n$.
And so our desired answer is
\begin{equation}
	3T\floor{\frac{n-1}{3}} + 5T\floor{\frac{n-1}{5}} - 15T\floor{\frac{n-1}{15}}.
\end{equation}
The complexity of this solution is $O(1)$, because our answer is just a computation.

## Other Solutions

A brute-force solution that adds each number $i$ from 1 to $n-1$ to a count if $i$ is divisible by 3 *or* 5 would have time complexity $O(n)$.
With the large input sizes of the Hackerrank problem ($n \le 10^9$) this solution is too slow, but it easily passes the original Project Euler problem.