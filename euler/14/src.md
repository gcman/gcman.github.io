‐‐‐
title: Problem 14 - Longest Collatz Sequence
date: 10 June 2018
category: euler
tags: proof
slug: euler/14
summary: My solution to problem 14 of Project Euler.
‐‐‐

# Problem Statement

The following iterative sequence is defined for the set of positive integers:
\begin{equation*}
	\begin{cases}
		n \to \frac{n}{2} \quad n \,\text{even}, \\
		n \to 3n + 1 \quad n\,\text{odd}
	\end{cases}
\end{equation*}
Using the rule above and starting with 13 generates the following sequence:
\begin{equation}
	13 \to 40 \to 20 \to 10 \to 5 \to 16 \to 8 \to 4 \to 2 \to 1
\end{equation}
This sequence contains 10 terms.
It is conjectured that every starting number produces a sequence that ends in 1.

Which starting number at most $N$ produces the longest chain?
If there are many possible such numbers, print the maximum one.

# My Algorithm

This problem is perfect for caching (or memoization) and recursion.
We define a recursive function that returns the length of a Collatz chain with a given starting number.
The function also store the chain length for each starting number (and, because the function is recursive, each number in the chain) in a list so that we do not have to compute it again.
Because of memory constraints, we do not store chain lengths for numbers greater than the maximum given $N$.
Instead, we compute these values on the fly.

We can then iterate over all possible starting numbers and keep a list of starting numbers which produce a right-maximal chain length (that is, they produce a chain length greater than or equal to all lenghts produced by smaller starting numbers).
Finally, we perform a binary search for the greatest element in this list less than each query.
This solution has time complexity $O(M + T\log M)$, where $M$ is the maximum possible starting value and $T$ is the number of queries.


## Other Solutions

Solutions which do not use memoization are too slow.