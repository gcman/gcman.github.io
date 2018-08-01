---
title: Problem 28 - Number Spiral Diagonals
date: 13 June 2018
category: euler
tags: primes
slug: euler/28
problem: 28
summary: My solution to problem 28 of Project Euler.
---

# Problem Statement

Starting with the number 1 and moving to the right in a clockwise direction, a 5-by-5 spiral is formed:

It can be verified that the sum of the numbers on the diagonals is 101.
What is the sum of the numbers on the diagonals in an $N \times N$ spiral ($N$ odd)?
Report your answer modulo $10^9 + 7$.

# My Algorithm

We can think of the spiral as being made up of a central 1 surrounded by $n$ rings of side length $2n+1$, where $n = \frac{N - 1}{2}$.
Let us derive a formula for the sum of the numbers in the corners of each ring---these make up the diagonals of the spiral.
The number in the top-right corner of the $n$-th ring is $(2n+1)^2$, the area of the ring.
Going counter-clockwise, the number decreases by one less than the side length, or $2n+1-1=2n$, each time.
And so the $n$-th ring has corner sum
\begin{equation}
	4(2n+1)^2 - 6(2n) = 16n^2 + 4n + 4.
\end{equation}

To find the sum of the corners of all rings, we can use the formula for the sum of the first $n$ natural numbers
\begin{equation}
	\sum_{i=0}^n i = \frac{n(n+1)}{2}
\end{equation}
and their squares:
\begin{equation}
	\sum_{i=0}^n i^2 = \frac{n(n+1)(2n+1)}{6}.
\end{equation}
To get the sum of the diagonals, we just add 1 to the sum of the corners, to account for the central 1.

And so our desired answer $S$ is
\begin{equation}
	\begin{split}
		S &= 1 + \sum_{i=0}^{\frac{N-1}{2}} (16n^2 + 4n + 4) \\
		&= 1 + 16\cdot\frac{\frac{N-1}{2}\left(\frac{N-1}{2} + 1\right)\left(2\cdot\frac{N-1}{2} + 1\right)}{6} + 4\cdot\frac{\frac{N-1}{2}\left(\frac{N-1}{2}+1\right)}{2} + 4\frac{N-1}{2} \\
		&= 1 + 4\cdot\frac{(N-1)(N - 1 + 2)(N - 1 + 1)}{6} + \frac{(N-1)(N-1+2)}{2} + 2(N-1) \\
		&= 1 + \frac{2N(N-1)(N+1)}{3} + \frac{(N-1)(N+1)}{2} + 2(N-1) \\
		&= \frac{4N(N-1)(N+1) + 3(N-1)(N+1) + 12(N-1) + 6}{6} \\
		&= \frac{4N^3 + 3N^2 + 8N - 9}{6}.
	\end{split}
\end{equation}
We report our answer modulo $10^9 + 7$.
Because there is a division by 6 in our answer, we must use the multiplicative modular inverse of 6 modulo $10^9 + 7$, which we find in $O(\log P)$ time.
And so our solution has time complexity $O(1)$.