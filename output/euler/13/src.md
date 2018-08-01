---
title: Problem 13 - Large Sum
date: 10 June 2018
category: euler
tags: brute-force
slug: euler/13
problem: 13
summary: My solution to problem 13 of Project Euler.
---

# Problem Statement
Find the first ten digits of the sum of $N$ 50-digit numbers.

# My Algorithm

Thanks to Python's built-in ability to handle infinitely large integers, this problem is a piece of cake.
We read in the numbers, add them, convert the result to a string, and output the first ten characters.

## Other Solutions

In languages without big integer support, we would need an algorithm to add big integers, using string arrays and the carrying method often taught in elementary schools.