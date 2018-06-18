‐‐‐
title: Problem 9 - Special Pythagorean Triplets
date: 10 June 2018
category: euler
tags: proof
slug: euler/9
problem: 9
summary: My solution to problem 9 of Project Euler.
‐‐‐

# Problem Statement

A Pythagorean triplet is a set of three natural numbers, $a < b < c$, for which,
\begin{equation*}
	a^2 + b^2 = c^2
\end{equation*}
For example, $3^2 + 4^2 = 9 + 16 = 25 = 52$.

Given $N$, find the maximal product $abc$ such that $a,b,c$ form a Pythagorean triplet for which $a+b+c = N$.
If no such triplet exists, output $-1$.

# My Algorithm

We know
\begin{equation}
	a + b + c = N
	\label{1}
\end{equation}
and
\begin{equation}
	a^2 + b^2 = c^2.
	\label{2}
\end{equation}
From \eqref{1} we get $c = N - a - b$, which we substitute into \eqref{2} to get
\begin{equation}
	\begin{split}
		a^2 + b^2 &= (N - (a + b))^2 \\
		a^2 + b^2 &= N^2 - 2N(a+b) + (a+b)^2 \\
		a^2 + b^2 &= a^2 + b^2 + 2ab + N^2 - 2Na - 2Nb \\
		0 &= b(2a - 2N) + N^2 - 2Na \\
		b(2a - 2N) &= 2Na - N^2 \\
		b &= \frac{N^2 - 2Na}{2N - 2a}.
	\end{split}
\end{equation}

Now we have expressions for $b,c$ in terms of $a$.
Note furthermore that because $a < b < c$ and $a + b + c = N$, none of the sides can exceed $\frac{N}{3}$.
Now we can iterate over $1 \le a \le \frac{N}{3}$ and store the maximal product $abc$ for which $a^2 + b^2 = c^2$.
This solution is $O(n)$.

## Other Solutions

We can also use preprocessing for an $O(N^2 + T)$ solution, where $T$ is the number of queries.
For all $a < b < 3000$, we check whether $c = \sqrt{a^2 + b^2}$ is an integer.
If so, we check whether $abc$ is greater than our existing answer for the perimeter $a + b + c$, which is by default $-1$.
To answer the queries, we look up the corresponding value in $O(1)$ time.