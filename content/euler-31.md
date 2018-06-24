title: Problem 31 - Coin Sums
date: 24 June 2018
category: euler
tags: dp
slug: euler/31
problem: 31
summary: My solution to problem 31 of Project Euler.

# Problem Statement

In England, the currency is made up of pounds (£) and pence (p), and there are eight coins in general circulation: 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:
\begin{equation*}
	1\cdot\mathrm{£}1 + 1\cdot50\mathrm{p} + 2 \cdot 20\mathrm{p} + 1 \cdot 5\mathrm{p} + 1 \cdot 2\mathrm{p} + 3\cdot1\mathrm{p}
\end{equation*}

In how many ways can $N$ pence be made from any denomination of coins? Output your answer modulo $10^9 + 7$.

# My Algorithm

This problem is a classic application of dynamic programming, the technique of breaking up a problem into smaller, reusable chunks.
To make $N$ pence, we can first make $N - c$ pence, then add one $c$ pence coin, where $c$ is the value of some denomination.
Then the number of ways we can make $N$ pence is the sum of $N - c$ over all valid $c$.

Using this principle, our solution is simple.
We maintain a list `coins` such that `coins[n]` is the number of ways we can make $n$ pence, where $0 \le n \le N$.
Then, for each valid denomination of coins $c$, we loop over $c \le n \le N$ and increment `coins[n]` by `coins[n-c]`.
At each step, we perform addition modulo $10^9 + 7$.

Because we maintain the list for all $0 \le n \le N_{\text{max}}$, we can answer each query in $O(1)$ time.
And so our solution has time complexity $O(CN_{\text{max}} + T)$, where $C$ is the number of coins and $T$ is the number of queries.