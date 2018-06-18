title: Problem 23 - Non-abundant Sums
date: 12 June 2018
category: euler
tags: brute-force
slug: euler/23
problem: 23
summary: My solution to problem 23 of Project Euler.

# Problem Statement

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number $n$ is called deficient if the sum of its proper divisors is less than $n$ and it is called abundant if this sum exceeds $n$.

As 12 is the smallest abundant number, $1 + 2 + 3 + 4 + 6 = 16$, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Given $N$, print `YES` if it can be written as the sum of two abundant numbers.
Otherwise, print `NO`.

# My Algorithm

We calculate $d(n)$ with trial division up to $\sqrt{n}$ as in [Problem 21](../21/).
We then make a list of abundant numbers by checking each number up to 28123, because any abundant number above this will not help us solve the problem.

To answer the problem, we need a function to decide whether a number $n$ can be written as the sum of two abundant numbers.
If $n > 28123$, we print `YES`; we are given this information in the problem, and without it, our solution is too slow to pass.
We make a new list whose elements are $n - a$ for an abundant number $a$.
If the intersection of this list and the list of abundant numbers is empty, then we print `NO`; otherwise, we print `YES`.
This solution has time complexity $O(n\sqrt{n} + AT)$, where $T$ is the number of queries and $A$ is the number of abundant numbers under 28123.