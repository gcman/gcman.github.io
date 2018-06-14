‐‐‐
title: Problem 24 - Lexicographic Permutations
date: 13 June 2018
category: euler
tags: proof
slug: euler/24
summary: My solution to problem 24 of Project Euler.
‐‐‐

# Problem Statement

A permutation is an ordered arrangement of objects.
For example, $\mathrm{dabc}$ is a permutation of the word $\mathrm{abcd}$.
If the permutations are listed alphabetically, we call it lexicographic order.
The lexicographic permutations of $\mathrm{abc}$ are:
\begin{equation*}
	\mathrm{abc}, \mathrm{acb}, \mathrm{bac}, \mathrm{bca}, \mathrm{cab}, \mathrm{cba}.
\end{equation*}
What is the $N$-th lexicographic permutation of the word $\mathrm{abcdefghijklm}$?

# My Algorithm

Suppose our word has $n$ letters.
Then the first $(n-1)!$ lexicographic permutations begin with $a$, the next $(n-1)!$ with $b$, and so on.
Consider the first $(n-1)!$ lexicographic permutations.
They consist of $a$ followed by a lexicographic permutation of the word without $a$.
Of these, the first $(n-2)!$ begin with $b$.

We can write $N$ as a unique sum
\begin{equation}
	N = \sum_{i=0}^{n-1} c_i \cdot i!,
\end{equation}
where $0 \le c_i \le i + 1$.
This is a kind of ``base-factorial'' expansion of $N$.
Once we do this, we use the procedure above.
Starting from $n-1$ and going down to $0$, the $N$-th lexicographic permutation has the $c_{n-1}$-th letter in the first position, the $c_{n-2}$-th letter of those remaining in the second position, and so on.

And so our algorithm is as follows.
Write $N$ as a sum of factorials.
Maintain a list of the letters in the word, in alphabetical order.
For $n-1 \ge i \ge 0$, delete the $c_i$-th element from the list and add it to the string representing the lexicographic permutation.
This solution has time complexity $O(L)$, where $L$ is the length of the given word.