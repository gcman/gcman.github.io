title: Problem 46 - Goldbach's Other Conjecture
date: 24 June 2018
category: euler
tags: proof
slug: euler/46
problem: 46
summary: My solution to problem 46 of Project Euler.

# Problem Statement

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
It turns out that the conjecture was false.
How many ways can a given $N$ be represented as the sum of a prime and twice a square?

# My Algorithm

Suppose an odd composite number $n$ and a prime $p$ provide a match.
Then $n = p + 2k^2$ for some positive integer $k$.
And so
\begin{equation}
	\begin{split}
		n - p &= 2k^2 \\
		k &= \sqrt{\frac{n-p}{2}}.
		\label{cand}
	\end{split}
\end{equation}
The numbers $n,p$ give a valid match if and only if \eqref{cand} is a positive integer.

We generate a list of primes up to $N_{\text{max}}$.
Then, we test every prime $p < N$ to see if \eqref{cand} is a positive integer; if so, we have found a valid way of representing $N$.
This solution has time complexity $O(N\log\log N + \frac{TN}{\log N})$, where $T$ is the number of queries.

## Project Euler

To solve the Project Euler problem, we write a while loop using the function `ways`.
We increment our index $i$, which is initialized at 3, until $i$ is composite.
Then, if `ways(i) == 0`, we break the loop; we have found the smallest number that cannot be represented as Goldbach conjectured.
Otherwise, we increment $i$ by 2.