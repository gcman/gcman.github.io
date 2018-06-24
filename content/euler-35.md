title: Problem 34 - Digit Factorials
date: 24 June 2018
category: euler
tags: brute-force
slug: euler/34
problem: 34
summary: My solution to problem 34 of Project Euler.

# Problem Statement

145 is a curious number, as $1! + 4! + 5! = 145$.
Find the sum of all numbers that are the sum of the factorials of their digits.
Note that $1! = 1$ and $2! = 2$ are not sums, as they contain only one digit.

# My Algorithm

We use a combinatorial approach similar to [Problem 30](../30/).
The sum of the factorials of the digits of a number with $d$ digits is $d\cdot9!$.
So the upper bound on the number we need to check is $7\cdot9!$, because $8\cdot9!$ only has 7 digits.
This means we can test valid candidate sets of size $2 \le k \le 7$ chosen with replacement from $0!,\ldots,9!$.

Like in Problem 30, we use multisets to check whether a combination is valid.
And so we perform\begin{equation}
	\sum\limits_{k=2}^{7} \mkern-5mu \binom{9+k}{k} = 19347
	\label{operations}
\end{equation}
operations, as in Problem 30.

## HackerRank

The HackerRank problem is, for once, much easier than the original Project Euler problem.
It asks us to find the sum of all $n < N$ such that $n$ divides its factorial digit sum.
Because $N \le 10^5$, we can run a brute force search, checking whether each $n < N$ is a valid solution.