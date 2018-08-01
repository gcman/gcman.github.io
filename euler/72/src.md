‐‐‐
title: Problem 72 - Counting Fractions
date: 22 July 2018
category: euler
tags: proof
slug: euler/72
problem: 72
summary: My solution to problem 72 of Project Euler.
‐‐‐

# Problem Statement

The fraction $\frac{a}{b}$ is called a reduced proper fraction if $a$ and $b$ are positive integers with $a < b$ and $\mathrm{gcd}(a,b) = 1$.
If we list the reduced proper fractions for $b \le 8$ in increasing order, we get
\begin{equation*}
	\frac18, \frac17, \frac16, \frac15, \frac14, \frac27, \frac13, \frac38, \frac25, \frac37, \frac12, \frac47, \frac35, \frac58, \frac23, \frac57, \frac34, \frac45, \frac56, \frac67, \frac78 
\end{equation*}
How many elements are contained in the set of reduced proper fractions with denominator at most $N$?

# My Algorithm

In order for a fraction to be in reduced form, the numerator and denominator must be coprime.
And so there are $\varphi(n)$ fractions with denominator $n$.
This is true for all $n$ except for 1, which does not contribute any fractions, because we only consider the elements of $\mathbb{Q} \cap (0,1)$.
In total, there are
\begin{equation}
	\sum\limits_{n=1}^N \varphi(n) - 1
\end{equation}
fractions.

We use Euler's product formula for the totient function:
\begin{equation}
	\varphi(n) = \prod\limits_{p|n}\left(1 - \frac{1}{p}\right).
\end{equation}
We can calculate this by using successive subtractions, starting from $n$.
For example, the primes that divide 15 are 3 and 5.
This gives $15 - \frac{15}{3} = 10 \to 10 - \frac{10}{5} = 8 = \phi(n)$.

We initialize an array `phi` of $n$ `0`-entries.
This accounts for $\varphi(1)$, which we do not wish to include in our final count.
Then, we use a method similar to the Sieve of Eratosthenes.
If `phi[n] = 0`, we have not yet dealt with $n$ and its multiples.
Because $n$ is prime, we set `phi[n] = n - 1`.
For all other multiples $kn < N$, we account for $n$ being a prime factor by setting `phi[k*n] -= phi[k*n]//n`.
Then, we sum the entries of `phi`, and add 1.

To give our final answer, we sum `phi[n]` for all $n < N$.
Doing this once for each test case would have time complexity $O(Tn\log\log n)$.
There are too many test cases for this, so we create a prefix sum array.

And so our solution has time complexity $O(n\log\log n + T)$, where $T$ is the number of test cases.