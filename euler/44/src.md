‐‐‐
title: Problem 44 - Pentagon Numbers
date: 16 July 2018
category: euler
tags: brute-force
slug: euler/44
problem: 44
summary: My solution to problem 44 of Project Euler.
‐‐‐

# Problem Statement

Pentagonal numbers are given by the formula
\begin{equation*}
	P_n = \frac{n(3n-1)}{2}.
\end{equation*}
The first ten pentagonal numbers are
\begin{equation}
	1,5,12,22,35,51,70,92,117,145,\ldots
\end{equation}
It can be seen that $P_4 + P_7 = 22 + 70 = 92 = P_8$.
Also, $P_7 - P_5 = 70 - 35 = 35 = P_5$ is also pentagonal.

Generalizing for a given $k$, find all $P_n$, where $n < N$, such that at least one of $P_n \pm P_{n-k}$ is pentagonal.

# My Algorithm

Using the formula for $P_n$, we find a formula for its inverse:
\begin{equation}
	\begin{split}
		2P_n &= 3n^2 - n \\
		n &= \frac{1 \pm \sqrt{1 + 4\cdot3\cdot2P_n}}{6}.
	\end{split}
\end{equation}
Because $n$ must be positive, we have that $x$ is a pentagonal number if and only if
\begin{equation}
	\frac{1 + \sqrt{24x + 1}}{6}
\end{equation}
is an integer.

From here we use a brute force approach.
For each $K < n < N$, test whether one of $P_n \pm P_{n-k}$ is pentagonal.
This solution has time complexity $O(N - K)$.

## Project Euler

The Project Euler version of this problem is more involved.
We must instead find the first $P_n$ such that both $P_n - P_{n-k}$ and $P_n + P_{n-k}$ are pentagonal.
To do this, we check all $k < n$ for each $n$ until we find the answer.
I used the following code, along with the same `pent` and `is_pent` functions as in the HackerRank solution:

```python
n = 0
while True:
	n += 1
	a = pent(n)
	for k in range(1,n):
		b = pent(n-k)
		if pent(a-b) and pent(a+b):
			print(a-b)
			break
```