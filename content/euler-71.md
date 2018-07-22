title: Problem 71 - Ordered Fractions
date: 21 July 2018
category: euler
tags: proof
slug: euler/71
problem: 71
summary: My solution to problem 71 of Project Euler.


# Problem Statement

The fraction \frac{a}{b} is called a reduced proper fraction if $a$ and $b$ are positive integers with $a < b$ and $\mathrm{gcd}(a,b) = 1$.
If we list the reduced proper fractions for $b \le 8$ in increasing order, we get
\begin{equation*}
	\frac18, \frac17, \frac16, \frac15, \frac14, \frac27, \frac13, \frac38, \frac25, \frac37, \frac12, \frac47, \frac35, \frac58, \frac23, \frac57, \frac34, \frac45, \frac56, \frac67, \frac78 
\end{equation*}
It can be seen that $\frac25$ is the fraction immediately to the left of $\frac37$. 

By listing the set of reduced proper fractions with denominator at most $N$ in increasing order, find the numerator and denominator of the fraction immediately to the left of $\frac{a}{b}$.

# My Algorithm

Let the sequence of reduced proper fractions with denominator at most $n$ listed in increasing order be the $n$-th [Farey sequence](https://en.wikipedia.org/wiki/Farey_sequence), $F_n$.
We will show that if $\frac{c}{d}$ directly precedes $\frac{a}{b}$ in $F_n$, then $ad - bc = 1$.

Because $\mathrm{gcd}(a,b) = 1$, the equation
\begin{equation}
	ay - bx = 1
	\label{dioph}
\end{equation}
has infinitely many integer solutions, by Bezout's theorem.
In particular, if $(x_0,y_0)$ is a solution, so is $(x_0 + ak, y_0 + bk)$.
Let us choose $k$ such that $n - b < y_0 + br \le n$.
And so there exists a solution $(x,y)$ such that
\begin{equation}
	0 \le n - b < y \le n.
	\label{fundineq}
\end{equation}
Suppose $\mathrm{gcd}(x,y) = d$.
Because $d|x,d|y$, we have $d|(ay - bx)$, and so $d | 1$.
This implies that $x$ and $y$ are coprime.
Because of this and the fact that $y \le n$, we have $\frac{x}{y} \in F_n$.
Furthermore,
\begin{equation}
	\frac{a}{b} > \frac{a}{b} - \frac{1}{by} = \frac{ay - 1}{by} = \frac{bx}{by} = \frac{x}{y}.
\end{equation}
And so $\frac{x}{y}$ precedes $\frac{a}{b}$.

Suppose $(x,y) \neq (c,d)$.
Then $\frac{x}{y}$ precedes $\frac{c}{d}$, and
\begin{equation}
	\frac{c}{d} - \frac{x}{y} = \frac{cy - dx}{dy} \ge \frac{1}{dy}.
	\label{ineq1}
\end{equation}
On the other hand,
\begin{equation}
	\frac{a}{b} - \frac{c}{d} = \frac{ad - bc}{bd} \ge \frac{1}{bd}.
	\label{ineq2}
\end{equation}
Applying \eqref{dioph} gives
\begin{equation}
	\frac{1}{xy} = \frac{ay - bx}{by} = \frac{a}{b} - \frac{x}{y}.
	\label{step1}
\end{equation}
Applying the sum of \eqref{ineq1} and \eqref{ineq2} to \eqref{step1} gives
\begin{equation}
	\begin{split}
		\frac{a}{b} - \frac{x}{y} &\ge \frac{1}{dy} + \frac{1}{bd} \\
		&= \frac{b+y}{bdy}.
	\end{split}
\end{equation}
By \eqref{fundineq} and the above, we thus have $\frac{1}{by} > \frac{n}{bdy}$.
Because $d < n$, we obtain the contradiction $\frac{1}{by} > \frac{1}{by}$.
Thus $(x,y) = (c,d)$.
This proves the result that $ad - bc = 1$.

Given $a,b$, we must solve for $ad - bc = 1$ such that $d$, the denominator, is maximized.
We can do this using the extended Euclidean algorithm.
Suppose $k$ is the multiplicative inverse of $a$ modulo $b$.
Then $ak \equiv 1 \pmod b$.
This means $ak - bj = 1$, for some positive integer $j$.
We wish to maximize $k$.
Given that $(k,j)$ is a solution, so is $(k+nb,j+na)$.
Thus we set
\begin{equation}
	\begin{split}
		k + nb &\le N \\
		n &\le \frac{N-k}{b} \\
		n &= \left\lfloor \frac{N-k}{b} \right\rfloor.
	\end{split}
\end{equation}
Solving for $j$, we get $j = \frac{a\left\lfloor \frac{N-k}{b} \right\rfloor + ak - 1}{b}$.
 solution is
\begin{equation}
	(c,d) = \left(\left\lfloor \frac{ab\left\lfloor \frac{N-k}{b} \right\rfloor + ak - 1}{b} \right\rfloor, b\left\lfloor \frac{N-k}{b} \right\rfloor + k \right).
\end{equation}

The only expensive part of this procedure is calculating the modular inverse, and so our solution has $O(\log b)$ time complexity.