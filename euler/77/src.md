‐‐‐
title: Problem 77 - Counting Summations
date: 23 July 2018
category: euler
tags: dp
slug: euler/77
problem: 77
summary: My solution to problem 77 of Project Euler.
‐‐‐

# Problem Statement

It is possible to write 10 as the sum of primes in exactly 5 different ways:
\begin{equation*}
	\begin{split}
		10 &= 7+3 \\
		&= 5+5 \\
		&= 5+3+2 \\
		&= 2+2+1 \\
		&= 3+3+2+2 \\
		&= 2+2+2+2+2
	\end{split}
\end{equation*}
How many ways can $N$ be written as the sum of primes?

# My Algorithm

Please see my solution to [Project Euler 31](../31/), as we use the same dynamic programming techniques.
This problem is a variant on the coin sum problem in Euler 31.
Here the coins take on the values of the primes up to $N$.
There are about $\frac{N}{\log N}$ primes up to $N$.
Our solution has time complexity $O(\frac{N^2}{\log N} + T)$.