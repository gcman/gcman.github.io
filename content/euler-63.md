title: Problem 63 - Powerful Digit Counts
date: 16 July 2018
category: euler
tags: proof
slug: euler/63
problem: 63
summary: My solution to problem 63 of Project Euler.

# Problem Statement

The five-digit number $16807 = 7^5$ is also a fifth power.
Given $N$, find the $N$-digit positive integers that are also an $N$-th power.

# My Algorithm

An $n$-digit $n$-th power has $n$-th root at most 9, because $10^n$ is an $(n+1)$-digit number.
If $a^n$ is an $n$-digit number, then unless $a = 9$, we also have that $(a+1)^n$ is an $n$-digit number.
We must find the lowest $a$ such that $a^n$ has $n$ digits.
We have
\begin{equation}
	\begin{split}
		10^{n-1} &\le a^n < 10^{n} \\
		10^{1-\frac{1}{n}} &\le a < 10 \\
		a &= \lceil10^{1-\frac{1}{n}}\rceil.
	\end{split}
\end{equation}
And so $k^n$ is an $n$-digit number for all $k \in [\lceil10^{1-\frac{1}{n}}\rceil,9]$.
We enumerate these in $O(1)$ time.