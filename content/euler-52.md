title: Problem 52 - Permuted Multiples
date: 16 July 2018
category: euler
tags: brute-force
slug: euler/52
problem: 52
summary: My solution to problem 52 of Project Euler.

# Problem Statement

It can be seen that the number $125874$ and its double, $251748$, contain exactly the same digits, but in a different order.
Given $N$, find all the positive integers up $x \le N$ such that $2x,3x,\ldots,Kx$ contain the same digits.

# My Algorithm

To check whether two strings are permutations of each other, we can check if they are equal after sorting.
To check whether an array contains only strings that are permutations of each other, we take the first element of the array and apply the above procedure to each other string in the array.

For each $125874 \le n \le N$, we create an array of the first $K$ multiples of $n$.
We use the described procedure to check if they all contain the same digits.
To speed this up, we only proceed with $n$ if $n$ and $Kn$ contain the same number of digits.
A further optimization is to check that each digit of $n$ is unique.