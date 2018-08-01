---
title: Problem 36 - Double Base Palindromes
date: 24 June 2018
category: euler
tags: brute-force
slug: euler/36
problem: 36
summary: My solution to problem 36 of Project Euler.
---

# Problem Statement

The decimal number $65 = 1001001001_2$ is palindromic in both decimal and binary.
Find the sum of all natural numers less than $N$ which are palindromic in base 10 and base $K$.

# My Algorithm

We need two things to solve this problem: a way to convert a number from base 10 to base $K$ and a way to generate palindromes.
First, let's think about how numbers are written in base 10.
The first thing we process is the rightmost digit, which represents the number of times the corresponding power of 10 goes into the number.
And so we must start with the highest power of the base, remove as many multiples of it as possible, and continue.
This procedure has $\lfloor\log_K n\rfloor$ steps, where $n$ is the decimal number to be converted.
This is because we perform one step for each possible exponent, where the maximal exponent on $K$ is $\lfloor \log_K n \rfloor$.

To generate palindromes of length at most $n$, we start with all numbers of length at most $\frac{n}{2}$.
To generate palindromes of even length at most $n$, we take one of these numbers $p$ and add on the reverse of $p$.
For odd-length palindromes, we do the same thing, but add one of the digits $0,\ldots,9$ in the middle.
And so there are $9\cdot10^{k-1}$ palindromes with $2k$ digits and $9\cdot10^{k}$ palindromes with $2k + 1$ digits.

Given $N$, we generate all palindromes with no more digits than $N$ and keep the ones less than $N$.
We test whether each of these are palindromic in base $K$.
We calculate less than $10^{\frac{\lfloor\log_K n\rfloor}{2}} \le \sqrt{n}$ palindromes and perform $\lfloor\log_K n\rfloor \le \log_K n$ operations on each of them.
Our solution has time complexity $O(\sqrt{n}\log n)$.