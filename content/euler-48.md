title: Problem 48 - Self Powers
date: 16 July 2018
category: euler
tags: brute-force
slug: euler/48
problem: 48
summary: My solution to problem 48 of Project Euler.

# Problem Statement

The sum $1^1 + 2^2 + \cdots + 10^{10} = 10405071317$.
Find the last ten digits of
\begin{equation}
	\sum\limits_{n=1}^N n^n.
\end{equation}

# My Algorithm

This problem is a simple bignum computation.
Because we only need the last ten digits, it suffices to carry out all calculations modulo $10^{10}$.
In particular, we use modular exponentiation.
This solution has time complexity $O(N\log N)$.