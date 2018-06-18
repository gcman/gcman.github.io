‐‐‐
title: Problem 21 - Amicable Numbers
date: 12 June 2018
category: euler
tags: brute-force
slug: euler/21
problem: 21
summary: My solution to problem 21 of Project Euler.
‐‐‐

# Problem Statement

Let $d(n)$ be defined as the sum of proper divisors of $n$ (numbers less than $n$ that divide evenly into $n$).
If $d(a) = b$ and $d(b) = a$, where $a \neq b$, then $a$ and $b$ are an amicable pair and each of $a$ and $b$ are amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore $d(220) = 284$.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so $d(284) = 220$.

Evaluate the sum of the proper divisors under $N$.

# My Algorithm

The first thing we need is a way to calculate $d(n)$.
A brute force method that tests all numbers from $1$ to $n$ and checks whether they divide $n$ is too slow.
But if a number $d$ divides $n$, then $\frac{n}{d}$ also divides $n$.
In particular, one of $n$ and $\frac{n}{d}$ is less or equal than $\sqrt{n}$, and the other is greater than or equal to $\sqrt{n}$.
To see this, consider what would happen if both were smaller than $\sqrt{n}$.
Their product would be less than $n$; a similar contradiction arises if both were greater than $\sqrt{n}$.

And so we only need to check each number less than $\sqrt{n}$.
If it divides $n$, we add it to the sum that we will return.
We therefore find $d(n)$ in $O(\sqrt{n})$ time.

Then we can use preprocessing to answer each query in $O(1)$ time.
For each $1 \le x \le N_{\text{max}}$, if $x = d(d(x))$ and $x \neq d(x)$, then we add $x$ to a list of amicable numbers.
To answer each query, we simply add the amicable numbers less than the given $N$.
Our solution has time complexity $O(N\sqrt{N} + T)$, where $N$ is the maximum possible input value and $T$ is the number of queries.