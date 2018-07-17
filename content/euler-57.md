title: Problem 57 - Square Root Convergents
date: 16 July 2018
category: euler
tags: proof,brute-force
slug: euler/57
problem: 57
summary: My solution to problem 57 of Project Euler.

# Problem Statement

It is possible to show that $\sqrt{2}$ has the following infinite continued fraction expansion:
\begin{equation*}
	\sqrt{2} = 1 + \frac{1}{2+\frac{1}{2 + \frac{1}{2 + \cdots}}}
\end{equation*}
By expanding this for the first four iterations, we get the convergents of $\sqrt{2}$
\begin{equation*}
	\begin{split}
		1 + \frac{1}{2} &= \frac{3}{2} \\
		1 + \frac{1}{2 + \frac{1}{2}} &= \frac{7}{5} \\
		1 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}} &= \frac{17}{12} \\
		1 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2 + \frac{1}{2}}}} &= \frac{41}{29}.
	\end{split}
\end{equation*}
The next three convergents are $\frac{99}{70},\frac{239}{169}$, and $\frac{577}{408}$.
However, the eighth convergent, $\frac{1393}{985}$, is the first for which the number of digits in the numerator exceeds the number of digits in the denominator.

Print the convergent numbers $n \le N$ where this happens.

# My Algorithm

A common piece of notation for a continued fraction
\begin{equation}
	a_0 + \frac{1}{a_1 + \frac{1}{a_2 + \cdots}}
\end{equation}
is $[a_0;a_1,a_2,\ldots]$.

Because all the coefficients $a_i, i > 1$ in our case are 2, the continued fraction expansion for $\sqrt{2}$ is self-similar.
In particular, if one convergent is $\frac{p}{q}$, we can write the next as
\begin{equation}
	1 + \frac{1}{1+\frac{p}{q}} = 1 + \frac{q}{p+q} = \frac{p+2q}{p+q}. 
\end{equation}

Using this recurrence relation, we can easily compute the convergents and count which ones have a numerator with more digits than the denominator.
This solution has time complexity $O(N)$.