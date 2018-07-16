title: Problem 47 - Distinct Primes Factors
date: 16 July 2018
category: euler
tags: primes
slug: euler/47
problem: 47
summary: My solution to problem 47 of Project Euler.

# Problem Statement

The first two consecutive numbers to have distinct prime factors are $14 = 2\cdot7$ and $15 = 3\cdot5$.
The first three consecutive such numbers are
\begin{equation*}
	\begin{split}
		644 &= 2^2 \cdot 7 \cdot 23,\\
		645 &= 3 \cdot 5 \cdot 43,\\
		646 &= 2 \cdot 17 \cdot 19
	\end{split}
\end{equation*}

Given $N$, find all the sets of $K$ consecutive integers that each have exactly $K$ distinct prime factors.
Print the first number of each set in ascending order.

# My Algorithm

The mathematical notation for the number of distinct prime factors of $n$ is $\omega(n)$ ($\Omega(n)$ denotes the total number of prime factors, counting multiplicity).
We use a modified Sieve of Eratosthenes: instead of storing whether $n$ is prime, we store $\omega(n)$.
Whenever we hit an $n$ with $\omega(n) = 0$, we find all the multiples of $n$ less than $N$ and add one to the associated value.

Then, we search through all sets of $K$ consecutive elements in the array and check whether they all have exactly $K$ distinct prime factors. 