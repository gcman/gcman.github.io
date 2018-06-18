title: Problem 16 - Power Digit Sum
date: 11 June 2018
category: euler
tags: brute-force
slug: euler/16
problem: 16
summary: My solution to problem 16 of Project Euler.

# Problem Statement

What is the sum of the digits of $2^N$?

# My Algorithm

Python has built-in infinite precision integer arithmetic, so this problem is easily done.
We find $2^N$ using built-in modular exponentiation in $O(\log N)$ time.
The length of this number is $\lceil N\log_{10} 2 \rceil \in O(N)$.
And so our solution has complexity $O(N \log N)$.