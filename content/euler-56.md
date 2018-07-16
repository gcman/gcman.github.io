title: Problem 56 - Powerful Digit Sum
date: 16 July 2018
category: euler
tags: brute-force
slug: euler/56
problem: 56
summary: My solution to problem 56 of Project Euler.

# Problem Statement

Considering natural numbers $a,b \le N$, which number of the form $a^b$ has the maximum digital sum?

# My Algorithm

For each $a,b \le N$, we simply compute $a^b$ in $\log b$ time and store its digital sum if it is maximal so far.
This solution has time complexity $O(N^2\log N)$.