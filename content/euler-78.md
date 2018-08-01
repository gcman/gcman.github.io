title: Problem 78 - Coin Partitions
date: 31 July 2018
category: euler
tags: proof
slug: euler/78
problem: 78
summary: My solution to problem 78 of Project Euler.
status: draft

# Problem Statement

Let $p(n)$ represent the number of ways $n$ can be written as the sum of positive integers.
For example, $p(5) = 7$.
Given $N$, return $p(N)$ modulo $10^9 + 7$.

# My Algorithm

We cannot use the $O(n^2)$ technique given in [Project Euler 31](../31/).
Instead, we will make use of a wonderful piece of mathematics known as [Euler's pentagonal number theorem](https://en.wikipedia.org/wiki/Pentagonal_number_theorem).
It states that
\begin{equation}
	\prod_{k=1}^\infty (1-x^k) = \sum_{i \in \mathbb{Z}}(-1)^ix^{g_i},
\end{equation}
where $g_i$ is the $i$-th generalized pentagonal number, given by $g_n = \frac{n(3n-1)}{2}$ for $n = \pm1,\pm2,\pm3,\ldots$ (note that $n$ is positive then negative and so on).
In other words,
\begin{equation}
	(1-x)(1-x^2)(1-x^3) \cdots = 1 - x - x^2 + x^5 + x^7 - x^12 - x^15 + x^22 + \cdots
\end{equation}

To prove this, let's first define the series $A_n$ as
\begin{equation}
	A_n = 1 - x^{2n - 1} - \sum_{i=3}^\infty x^{in - 1} \prod_{j = 0}^{i-3} (1 - x^{n+j}).
\end{equation}
Factoring out an $x^{3n-1}$ term from the last summand gives
\begin{equation}
	A_n = 1 - x^{2n - 1} - x^{3n-1}\sum_{i=0}^\infty x^{in} \prod_{j = 0}^{i} (1 - x^{n+j}).
\end{equation}
Let us denote this new series as $B_n$, such that
\begin{equation}
	A_n = 1 - x^{2n - 1} - x^{3n-1}B_n.
\end{equation}
Pulling out the $i=j=0$ term from the series $B_n$ gives
\begin{equation}
	\begin{split}
		B_n &= \sum_{i=0}^\infty x^{in} \prod_{j = 0}^{i} (1 - x^{n+j}) \\
		&= x^0(1 - x^{n+0}) + \sum_{i=1}^\infty x^{in} (1-x^n)\prod_{j = 0}^{i} (1 - x^{n+j}) \\
		&= 1 - x^n + \sum_{i=1}^\infty x^{in} (1-x^n)\prod_{j = 1}^{i} (1 - x^{n+j}).
	\end{split}
\end{equation}
Distributing the $j = 0$ term we pulled out of the product, we have
\begin{equation}
	\begin{split}
		B_n &= 1 - x^n + \sum_{i=1}^\infty x^{in}\prod_{j = 1}^{i} (1 - x^{n+j}) - \sum_{i=1}^\infty x^nx^{in}\prod_{j = 1}^{i} (1 - x^{n+j}) \\
		B_n &= 1 - x^n + \sum_{i=1}^\infty x^{in}\prod_{j = 1}^{i} (1 - x^{n+j}) - \sum_{i=1}^\infty x^{(i+1)n}\prod_{j = 1}^{i} (1 - x^{n+j}) \\
	\end{split}
\end{equation}



It implies that
\begin{equation}
	\begin{split}
		p(n) &= \sum_k (-1)^{k-1}p(n-g_k) \\
		&= p(n-1) + p(n-2) - p(n-5) - p(n-7) + \cdots,
	\end{split}
\end{equation}


First, let's look at the generating function for $p(n)$.
We have
\begin{equation}
	\prod_{k=1}^\infty \left( \frac{1}{1-x^k} \right) = \sum_{k=0}^\infty p(k)x^k.
\end{equation}
To see why this is the case, let's expand each term of the product as a geometric series.
It will have first term 1 and common ratio $x^k$.
We then have
\begin{equation}
	\begin{split}
		\prod_{k=1}^\infty \left( \frac{1}{1-x^k} \right) &= (1 + x + x^2 + x^3 + \cdots)(1 + x^2 + x^4 + x^6 + \cdots)(1 + x^3 + x^6 + x^9 + \cdots)\cdots \\
		&= \prod_{k=1}^\infty \left( \sum_{j=0}^\infty x^{kj} \right).
	\end{split}
	\label{part-form}
\end{equation}
Consider the coefficient on the term $x^n$.
To get $x^n$, we take one summand from each term in the sum.
In other words, each term is of the form $x^{k_1 + 2k_2 + 3k_3 + \cdots}$.
A combinatorial interpretation is that each coefficient $k_i$ represents the number of times $i$ appears in a particular way of writing $n$ as a sum of natural numbers.
This means that the coefficient on $x^n$ is the number of such ways to write $n$, which is $p(n)$.