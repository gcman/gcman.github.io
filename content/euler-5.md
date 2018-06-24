title: Problem 5 - Smallest Multiple
date: 10 June 2018
category: euler
tags: primes
slug: euler/5
problem: 5
summary: My solution to problem 5 of Project Euler.

# Problem Statement

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to $N$?

# My Algorithm

For a number $a$ to divide another number $b$, each of the prime powers that divide $a$ must also divide $b$.
That is, the exponent on each of the prime powers that divide $a$ is less than or equal to the corresponding exponent on a prime power that divides $b$.
For each number from 1 to $N$ to divide a number $M$, each prime power less than $N$ must also divide $M$.
To minimize $M$, we have each prime $p \le N$ divide $M$ as many times as it does the largest prime power of $p$ at most $N$.
That is
\begin{equation}
	M = \prod_{p \le N} p^{\lfloor \log_pN \rfloor}.
\end{equation}
To compute our answer $M$, we need a list of the primes less than $N$, for which we can use the Sieve of Eratosthenes.
And so our solution has time complexity $O(n\log\log n)$.

## Other Solutions

This problem can also be phrased as finding the lowest common multiple of $1,\ldots,N$, for which the classic formula is $\mathrm{lcm}(1,\ldots,N) = \frac{N!}{\mathrm{gcd}(1,\ldots,N)}$.
Because the numerator grows very quickly, we can compute the LCM iteratively, making use of the fact that $\mathrm{lcm}(a,b,c) = \mathrm{lcm}(\mathrm{lcm}(a,b),c)$ and storing the latest LCM with each step.
This algorithm computes the greatest common denominator of two numbers at most $N$, which can be done in $O(\log n)$ time, $N$ times.
And so this solution has time complexity $O(n\log n)$.
However, it has much better space complexity, at $O(1)$, than the sieve of Eratosthenes, which needs $O(n)$ space to store an array of size $n$.
So for large $n$, this alternative solution is preferred.