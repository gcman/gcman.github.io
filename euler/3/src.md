‐‐‐
title: Problem 3 - Largest Prime Factor
date: 10 June 2018
category: euler
tags: proof
slug: euler/3
summary: My solution to problem 3 of Project Euler.
‐‐‐

# Problem Statement

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor a given number $N$?

# My Algorithm

Suppose we split $n$ into two factors.
Then one of them is at least $\sqrt{n}$ and the other is at most $\sqrt{n}$.
To see this, we argue by contradiction; if both were strictly less than $\sqrt{n}$, then their product would be strictly less than $n$, and if both were strictly greater, so would their product.
Of course, $n$ can't be greater than or less than itself.

This is a very valuable fact.
It means that if $n$ is not divisible by a prime at most $\sqrt{n}$, then $n$ is itself prime.
So if we have a list of the primes under $\sqrt{n}$, and divide $n$ as much as we can by each of them, then what is left is either 1 or the largest prime factor of $n$.
In the first case, the answer is the largest prime that divided $n$, which we can keep track of.

To generate the list of primes, we can use the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes), a classic tool in number theory.
We start with a list of the first $m$ numbers.
We cross out all the multiples of 2, then go to the next uncrossed number, and cross out all of its multiples.
When we cannot cross out any more numbers, we are left with the primes less than or equal to $m$.
The time complexity of this operation is $O(m\log\log m)$.
There are about $\frac{m}{\log m}$ primes under $m$, according to the [Prime Number Theorem](https://en.wikipedia.org/wiki/Prime_number_theorem).
In our case, $m = \sqrt{n}$.
And so the time complexity of our solution is $O(\sqrt{n}\log \log \sqrt{n} + \frac{n}{\log n}) = O(\sqrt{n} \log \log n)$.

## Other Solutions
Because we only need the *largest* prime factor, an $O(\sqrt{n})$ solution is possible.
The largest factor of $n$ must be prime.
So we check whether each numbers up to $\sqrt{n}$ divides $n$ and keep track of the largest so far that does, which is our answer.
However, the solution above gives more generally applicable techniques and can also be used to find the $k$-th largest prime factor.