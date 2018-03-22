---
title: Extending the Fibonacci Numbers
date: 19 March 2018
category: math
tags: fun
slug: fib-ext
status: draft
---

The Fibonacci numbers are probably the most well-known sequence in mathematics (of course, not including something like the counting numbers).
They have the property that each term is the sum of the two previous terms, and the first two terms are 0 and 1:
\begin{equation}
	0,1,1,2,3,5,8,13,21,34,55,\ldots
\end{equation}
This sequence is deeply connected with the golden ratio
\begin{equation}
	\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618034.
\end{equation}
For example, the ratio of the $n$-th Fibonacci number with the one before it tends to $\varphi$ as $n$ gets very large.

# Fibonacci and Phi
To examine this connection, let's look at the origins of the golden ratio; it describes two lengths $a$ and $b$ whose ratio is the same as the ratio between their sum and the larger of them.
That is,
\begin{equation}
	\frac{a+b}{a} = \frac{a}{b}.
\end{equation}
Let's let this expression equal $x$ and solve.
We first break up the left side.
\begin{equation}
	\begin{split}
		\frac{a+b}{a} &= 1 + \frac{b}{a} \\
		x &= 1 + \frac{1}{x} \\
		x^2 &= x + 1.
	\end{split}
	\label{phi-rel}
\end{equation}
Applying the quadratic formula, we find two values that satisfy this relation: $\frac{1+\sqrt{5}}{2}$ and $\frac{1-\sqrt{5}}{2}$.
The latter is negative, so it can't be the ratio between two positive lengths.
And so we've found $\varphi$, as well as its cousin.

Note that the powers of $\varphi$ satisfy the Fibonacci relation: each term is the sum of the previous two terms, as demonstrated in \ref{phi-rel}.