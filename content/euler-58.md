title: Problem 58 - Spiral Primes
date: 16 July 2018
category: euler
tags: primes,brute-force
slug: euler/58
problem: 58
summary: My solution to problem 58 of Project Euler.

# Problem Statement

Starting with 1 and spiralling clockwise in the following way, a square spiral with side length 7 is formed.

![A 7-by-7 number spiral.](../../figures/euler-58-spiral.png){ width=45% }

It is interesting to note that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of $\frac{8}{13} \approx 62\%$.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed.
If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below $N\%$?

# My Algorithm

As shown in my solution to [Project Euler 28](../28/), the corners of a number spiral of size $n$ are of the form $n^2 - i(n-1)$, for $i \in \{1,2,3,4\}$.
We discount the case where $i = 4$, because this is $(n+2)^2$.
We use the [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) to search such numbers and count the primes until the desired ratio is reached.
This solution has time complexity $O(N\log^3N)$, where $N$ is the maximum side length we must search.