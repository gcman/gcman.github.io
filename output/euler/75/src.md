‐‐‐
title: Problem 75 - Singular Integer Right Triangles
date: 23 July 2018
category: euler
tags: proof
slug: euler/75
problem: 75
summary: My solution to problem 75 of Project Euler.
‐‐‐

# Problem Statement

For how many values $P \le N$ is there exactly one way to form a right triangle with integer side lengths and perimeter $P$?

# My Algorithm

See my solution to [Project Euler 39](../39/), as the techniques I use there are exactly the ones I use for this problem.
The only difference is that we count only "singular" values of $P$, and we binary search on the index of the greatest value up to $N$.
Our solution has time complexity $O(N_{\text{max}} + T\log N_{\text{max}})$, where $T$ is the number of test cases.