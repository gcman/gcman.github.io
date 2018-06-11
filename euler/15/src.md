‐‐‐
title: Problem 15 - Lattice Paths
date: 11 June 2018
category: euler
tags: proof
slug: euler/15
summary: My solution to problem 15 of Project Euler.
‐‐‐

# Problem Statement

Suppose we start at the top-left corner of an $N\times M$ grid and that we can only travel to the right or down.
How many routes are there to the bottom-right corner?
Output the answer modulo $10^9 + 7$

# My Algorithm

In total, we must make $N+M$ moves, of which $N$ are to the right.
Choosing these $N$ moves uniquely identifies each possible route, as this is equivalent to choosing the $M$ downwards moves.
This is a combinatorial explanation for the fact that
\begin{equation}
	\binom{N+M}{N} = \binom{N+M}{M} = \frac{(N+M)!}{N!M!}
\end{equation}
which is our answer.
To make the computation easier, we use the smaller of $N$ and $M$.

Suppose we know the value of $\binom{a}{b} = \frac{a!}{b!(a-b)!}$.
Then we can find the value of
\begin{equation}
	\binom{a}{b+1} = \frac{a!}{(b+1)!(a-b-1)!} = \binom{a}{b}\frac{a-b}{b+1}
	\label{recurrence}
\end{equation}
This gives us a recurrence relation.
Because we are computing the answer modulo $10^9 + 7$, we must use the modular multiplicative inverse of $b+1$.
Because the modulus is prime, this is guaranteed to exist.
We can find this using the [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) in $O(\log P)$ time, where $P = 10^9 + 7$.

Starting with $\binom{N+M}{0} = 1$, we iterate over $0 \le k \le \mathrm{min}(N,M) - 1$ use the recurrence relation \eqref{recurrence}, multiplying by $N + M - k$ and the modular inverse of $k + 1$ under $P$.
At each step, we take the expression modulo $P$.
Our solution has time complexity $O(\mathrm{min}(N,M)\log P)$.