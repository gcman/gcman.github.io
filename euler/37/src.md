---
title: Problem 37 - Truncatable Primes
date: 24 June 2018
category: euler
tags: primes,brute-force
slug: euler/37
problem: 37
summary: My solution to problem 37 of Project Euler.
---

# Problem Statement

The number 3797 has an interesting property.
Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, 7.
Similarly, we can remove digits from right to left: 3797, 379, 37, 3.

Find the sum of primes that are truncatable from left to right and right to left less than $N$.

# My Algorithm

A prime is greater than all of its truncations.
This means that we can use a modified Sieve of Eratosthenes.
Whenever a prime is encountered, we can check if all its truncations are also prime; we will already have computed whether each truncation is prime.

When a number has not been marked in the sieve, we mark all of its multiples, like normal.
To right-truncate, we can keep performing integer division by 10.
To left-truncate, we first find the largest power of 10 that divides the prime.
Then, we take the prime modulo this power of 10, and decrement the power of 10 by one, and repeat.
We stop either truncation process when the value returned is not prime.

If at the end of both processes, the remaining value is 0, it means both truncations were completed and the prime is fully truncatable.
In this case, we add the prime to a running count.
This algorithm has time complexity $O(n\log\log n)$.