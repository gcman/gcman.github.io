title: Problem 65 - Convergents of $e$
shorttitle: Problem 65 - Convergents of e
date: 16 July 2018
category: euler
tags: proof
slug: euler/65
problem: 65
summary: My solution to problem 65 of Project Euler.

# Problem Statement

The constant $e$ can be written as the infinite continued fraction $[2;1,2,1,\,1,4,1,\,1,6,1,\ldots,1,2k,\ldots]$.
Find the sum of the digits in the $N$-th convergent of the continued fraction expansion for $e$.

# A Recurrence Relation

We will show the following theorem.
Let the the $n$-th convergent of a continued fraction $[a_0;a_1,a_2,\ldots]$ be $\frac{P_n}{Q_n}$.
Then the $(n+1)$-th convergent is
\begin{equation}
	\frac{a_{n+1}P_n + P_{n-1}}{a_{n+1}Q_{n} + Q_{n-1}}.
\end{equation}

We use induction.
Because the 0-th convergent is $a_0$, we define $P_0 = a_0, Q_0 = 1$.
Then the first convergent is
\begin{equation}
	a_0 + \frac{1}{a_1} = \frac{a_0a_1 + 1}{a_1},
\end{equation}
so $P_1 = a_0a_1 + 1, Q_1 = a_1$.
As a base case, we show that the formula holds for $n = 2$:
\begin{equation}
	\begin{split}
		a_0 + \frac{1}{a_1 + \frac{1}{a_2}} &= a_0 + \frac{a_2}{a_1a_2 + 1} \\
		&= \frac{a_0a_1a_2 + a_0 + a_2}{a_1a_2 + 1} \\
		&= \frac{a_2(a_0a_1 + 1) + a_0}{a_2a_1 + 1} \\
		&= \frac{a_2P_1 + P_0}{a_2Q_1 + Q_0}.
	\end{split}
\end{equation}

Now suppose inductively that
\begin{equation}
	P_{n} = a_{n}P_{n-1} + P_{n-2}, Q_{n} = a_nQ_{n-1} + Q_{n-2}.
\end{equation}
The $n$-th convergent is
\begin{equation}
	\frac{P_n}{Q_n} = a_1+\cfrac{1}{a_2+\cfrac{1}{\begin{array}{ccc}a_{3}+ & & \\& \ddots & \\& & +\cfrac{1}{a_{n-1}+\cfrac{1}{a_{n}}}\end{array}}}
	\label{n-conv}
\end{equation}
Turning \eqref{n-conv} into the $(n+1)$-th convergent involves replacing $a_n$ with $a_n + \frac{1}{a_{n+1}}$.
Using the recursive formula, this gives
\begin{equation}
	\begin{split}
		\frac{P_{n+1}}{Q_{n+1}} &= \frac{\frac{P_{n-1}}{a_{n+1}} + a_nP_{n-1} + P_{n-2}}{\frac{Q_{n-1}}{a_{n+1}} + a_nQ_{n-1} + Q_{n-2}} \\
		&= \frac{\frac{P_{n-1}}{a_{n+1}} + P_n}{\frac{Q_{n-1}}{a_{n+1}} + Q_n} \\
		&= \frac{a_{n+1}P_n + P_{n-1}}{a_{n+1}Q_{n} + Q_{n-1}},
	\end{split}
\end{equation}
which proves the theorem.

# My Algorithm

Let the $n$-th coefficient in the continued fraction expansion for $e$ be $a_n$.
Then $a_0 = 2$.
From then on, $a_1 = a_3 = 1$, and $a_2 = 2$.
In particular, $a_n = 1$ if $n$ is congruent to 0 or 1 mod 3 (unless $n = 0$).
And so
\begin{equation}
	a_n = 
	\begin{cases}
		2 &n = 0, \\
		2\left(\lfloor\frac{n}{3}\rfloor + 1\right) &n \equiv 2 \pmod 3, \\
		1 &\text{otherwise}.
	\end{cases}
\end{equation}

Using this and our theorem, we iteratively calculate the numerator of the $N$-th convergent by
\begin{equation}
	P_n = a_nP_{n-1} + P_{n-2}.	
\end{equation}
We cache the previous two convergents at each step.
Finally, we take the digit sum.
Our solution has time complexity $O(N)$.