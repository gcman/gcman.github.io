title: Problem 32 - Pandigital Products
date: 24 June 2018
category: euler
tags: brute-force
slug: euler/32
problem: 32
summary: My solution to problem 32 of Project Euler.

# Problem Statement

We shall say that an $N$-digit number is pandigital if it makes use of all the digits 1 to $N$ exactly once; for example, the 5-digit number 15234 is 1 through 5 pandigital.
The product 7254 is unusual, as the identity $39 \cdot 186 = 7254$ containing multiplicand, multiplier, and product is 1 through 9 pandigital.
Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through $N$ pandigital.

# My Algorithm

We use a brute-force check on all ways of splitting up a pandigital number into three non-empty parts.
We can generate each pandigital number by finding the permutations of a string with digits from $1$ to $N$.
There are $N!$ of these.
It is then simple to verify whether the product of the first two parts is equal to the third part.

Using the combinatorial technique of [stars and bars](https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)), there are $\binom{n-1}{k-1}$ ways to distribute $n$ indistinguishable objects among $k$ distinguishable groups.
Our groups---the three parts---are distinguishable, as their order matters.
For a given pandigital number, the digits cannot move, so they are thought of as indistinguishable.
And so there are $\binom{N-1}{2}$ ways of splitting up each pandigital number.

We know
\begin{equation}
	N! \binom{N-1}{2} = \frac{N!(N-1)!}{2(N-3)!} = \frac{N!(N-1)(N-2)}{2} \le \frac{N^2N!}{2}.
\end{equation}
And so our solution has time complexity $O(N^2N!)$.
