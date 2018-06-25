title: Problem 42 - Coded Triangle Numbers
date: 24 June 2018
category: euler
tags: proof
slug: euler/42
problem: 42
summary: My solution to problem 42 of Project Euler.

# Problem Statement

The $n$-th term of the sequence of triangle numbers is given by $t_n = \frac{n(n+1)}{2}$; so the first ten triangle numbers are
\begin{equation*}
	1,3,6,10,15,21,28,36,45,55,\ldots
\end{equation*}
By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is $19 + 11 + 25 = 55 = t_{10}$.

You are given a file `words.txt`.
Of the English words it contains, how many are triangle words?

# My Algorithm

Let us suppose we have some number $t = \frac{n(n+1)}{2}$.
Then
\begin{equation}
	\begin{split}
		2t &= n(n+1) \\
		2t &= n^2 + n \\
		n^2 + n - 2t &= 0 \\
		n &= \frac{-1 \pm \sqrt{8t + 1}}{2}.
	\end{split}
\end{equation}
Because we are solving for positive $n$, we have
\begin{equation}
	n = \frac{-1 + \sqrt{8t + 1}}{2}.
	\label{n}
\end{equation}
We know that $t$ is a triangle number if and only if \eqref{n} is an integer.

To compute the name scores, we use the same method as in [Problem 22](../22/).
To finish the problem, we read in the names, and count them if their score is a triangle number.
The time complexity of this solution is $O(n)$, where $n$ is the number of names.

## HackerRank

The HackerRank version of this problem is simpler.
It does not involve words.
Instead, it asks whether a number $n \le 10^{18}$ is triangular.
We have an $O(1)$ method of answering this question.