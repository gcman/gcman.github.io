‐‐‐
title: Problem 76 - Counting Summations
date: 23 July 2018
category: euler
tags: dp
slug: euler/76
problem: 76
summary: My solution to problem 76 of Project Euler.
‐‐‐

# Problem Statement

It is possible to write 5 as the sum of at least two positive integers in exactly 6 different ways:
\begin{equation*}
	\begin{split}
		5 &= 4+1 \\
		&= 3+2 \\
		&= 3+1+1 \\
		&= 2+2+1 \\
		&= 2+1+1+1 \\
		&= 1+1+1+1+1
	\end{split}
\end{equation*}
How many ways can $N$ be written as the sum of at least two positive integers?
Report your answer modulo $10^9 + 7$.

# My Algorithm

Please see my solution to [Project Euler 31](../31/), as we use the same dynamic programming techniques.
This problem is a variant on the coin sum problem in Euler 31.
This time, the coins have values $1,2,\ldots,N$.

At the end, we subtract 1 to exclude the vacuous sum which is just $N$ itself, and then we report our answer modulo $P$.
Our solution has time complexity $O(N^2 + T)$.