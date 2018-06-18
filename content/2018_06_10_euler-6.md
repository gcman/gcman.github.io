title: Problem 6 - Sum Square Difference
date: 10 June 2018
category: euler
tags: identity
slug: euler/6
problem: 6
summary: My solution to problem 6 of Project Euler.

# Problem Statement

The sum of the squares of the first ten natural numbers is
\begin{equation*}
	1^2 + 2^2 + \cdots + 10^2 = 385.
\end{equation*}
The square of the sum of the first ten natural numbers is
\begin{equation*}
	(1 + 2 + \cdots + 10)^2 = 55^2 = 3025
\end{equation*}
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is $3025 - 385 = 2640$.
Find the absolute difference between the sum of the squares of the first $N$ natural numbers and the square of the sum.

# My Algorithm

We make use of the following two formulas, which can be proven using induction.
\begin{equation}
	\sum_{i=1}^n i = \frac{n(n+1)}{2}
	\label{1}
\end{equation}
and
\begin{equation}
	\sum_{i=1}^n i^2 = \frac{n(n+1)(2n+1)}{6}.
	\label{2}
\end{equation}

Applying these two formulas, the desired value is
\begin{equation}
	\begin{split}
		\Big| \frac{n^2(n+1)^2}{4} - \frac{n(n+1)(2n+1)}{6} \Big| &= \Big|\frac{n^4+2n^3+n^2}{4} - \frac{2n^3 + 3n^2 + n}{6} \Big| \\
		&= \Big| \frac{3n^4+6n^3+3n^2}{12} - \frac{4n^3 + 6n^2 + 2n}{12} \Big| \\
		&= \Big| \frac{3n^4+2n^3-3n^2-2n}{12} \Big| \\
	\end{split}
	\label{final-sum}
\end{equation}
This value is non-negative for all positive integers, so the absolute value bars are not necessary.
Our algorithm is just a computation, so it has time complexity $O(1)$.

## Other Solutions

We did not need to simplify the expression as in \eqref{final-sum}; we could have simply subtracted \eqref{2} from the square of \eqref{1}.
An $O(n)$ solution is also possible: simply add the first $N$ numbers, square them, and subtract the sum of the squares of the first $N$ numbers.