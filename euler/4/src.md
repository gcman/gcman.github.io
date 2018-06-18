‐‐‐
title: Problem 4 - Largest Palindrome Product
date: 10 June 2018
category: euler
tags: brute-force
slug: euler/4
problem: 4
summary: My solution to problem 4 of Project Euler.
‐‐‐

# Problem Statement

A palindromic number reads the same both ways. The smallest 6 digit palindrome made from the product of two 3-digit numbers is $101101 = 143 \cdot 707$. 

Find the largest palindrome made from the product of two 3-digit numbers which is less than $N$.

# My Algorithm

There are less than $10^6$ possible products of two 3-digit numbers, so brute force is a possible solution.
We compute all products $ij$ of numbers $100 \le i,j \le 999$.
If they are palindromic (the reversed string of $ij$ is identical to the string of $ij$), we keep them.
Then we sort the palindromic products and perform a binary search for the greatest element of the array strictly less than $N$.
The only tricky thing here is to remember that if $N$ is in the array of palindromic products, we must return the element directly before $N$.