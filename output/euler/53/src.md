‐‐‐
title: Problem 53 - Combinatoric Selections
date: 16 July 2018
category: euler
tags: combinatorics
slug: euler/53
problem: 53
summary: My solution to problem 53 of Project Euler.
‐‐‐

# Problem Statement

How many, not necessarily distinct, values of $\binom{n}{r}$, for $n \le N$, are greater than $K$?

# My Algorithm

A brute-force search is too slow.
And so we exploit the symmetry of Pascal's triangle, which contains the binomial coefficients.
Because $\binom{n}{k} = \binom{n}{n-k}$, we need only check up to $\frac{n}{2}$.
Furthermore, if $\binom{n}{k}$ is the first value greater than $K$, then because the entries of Pascal's triangle strictly increase until the central term, all the entries between $k$ and $n-k$, inclusive, will be greater than $K$.
This amounts to $n-2k+1$.

We also make use of the recurrence relation
\begin{equation}
	\binom{a}{b+1} = \binom{a}{b}\frac{a-b}{b+1},
\end{equation}
as described in my solution to [Project Euler 15](../15/).

We iterate through the binomial coefficients in row $n$ until we find one greater than $K$, say $\binom{n}{i}$.
Then the answer is the sum of $n + 1 - 2i$ for each $n \le N$.
This solution has time complexity $O(N^2)$.