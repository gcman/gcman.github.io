---
title: Harmonic Numbers and Binomial Coefficients
date: 4 February 2018
category: math
tags: calculus, proof
slug: harm-id
status: draft
---

The $n$-th harmonic number is defined as the sum of reciprocals of the first $n$ natural numbers:
\begin{equation}
	\sum\limits_{k=1}^n \frac{1}{k}.
\end{equation}
We wish to prove the following identity involving harmonic numbers and binomial coefficients:
\begin{equation}
	\sum\limits_{k=1}^n \frac{1}{k} = -\sum\limits_{k=1}^n \frac{1}{k}\binom{n}{k}(-1)^k.
\end{equation}
I have two solutions: one with calculus, and one by induction.

# Calculus
First, we notice that
\begin{equation}
	\int_0^1 x^{k-1} \d x = \frac{x^k}{k} \Bigr\rvert_0^1 = \frac{1}{k} - \frac{0}{k} = \frac{1}{k}.
\end{equation}
Then
\begin{equation}
	\sum\limits_{k=1}^n \frac{1}{k} = \sum\limits_{k=1}^n \int_0^1 x^{k-1} \d x.
\end{equation}
Because this is a finite sum of converging integrals, we can switch the sum and the integral to get
\begin{equation}
	\int_0^1 \sum\limits_{k=1}^n x^{k-1} \d x.
\end{equation}
Notice that the sum is a geometric series:
\begin{equation}
	1 + x + x^2 + \cdots + x^{n-1} = \frac{1 - x^n}{1-x}.
\end{equation}
Then we can solve the integral, using the substitution $x = 1-u, \d x = -\d u$ and applying the binomial theorem:
\begin{equation}
	\begin{split}
		\int_0^1 \frac{1 - x^n}{1-x} \d x &= -\int_1^0 \frac{1 - (1-u)^n}{u} \d u \\
		&= \int_0^1 \frac{1}{u}\left( 1 - \sum\limits_{k=0}^n \binom{n}{k}(-1)^ku^k \right) \d x \\
		&= -\int_0^1 \frac{1}{u}\left(\sum\limits_{k=0}^n \binom{n}{k}(-1)^ku^k - 1 \right) \d x \\
		&= -\int_0^1 \frac{1}{u}\sum\limits_{k=1}^n \binom{n}{k}(-1)^ku^k \d x \\
		&= -\int_0^1 \sum\limits_{k=1}^n \binom{n}{k}(-1)^ku^{k-1} \d x \\
		&= -\sum\limits_{k=1}^n \binom{n}{k}(-1)^k\int_0^1 u^{k-1} \d x \\
		&= -\sum\limits_{k=1}^n \frac{1}{k}\binom{n}{k}(-1)^k.
	\end{split}
\end{equation}
This concludes our proof.

# Induction
We first show that
\begin{equation}
	\frac{1}{k+1}\binom{n}{k} = \frac{1}{n+1}\binom{n+1}{k+1}.
	\label{lemma-1}
\end{equation}
We use the factorial representation.
The left-hand side equals
\begin{equation}
	\frac{1}{k+1}\binom{n}{k} = \frac{1}{k+1}\frac{n!}{k!(n-k)!} = \frac{n!}{(k+1)!(n-k)!},
\end{equation}
while the right-hand side equals
\begin{equation}
	\frac{1}{n+1}\binom{n+1}{k+1} = \frac{1}{n+1}\frac{(n+1)!}{(k+1)!(n-k)!} = \frac{n!}{(k+1)!(n-k)!}.
\end{equation}
So \eqref{lemma-1} holds.
Next we show that
\begin{equation}
	\sum\limits_{k=0}^n \frac{1}{k+1} \binom{n}{k} (-1)^k = \frac{1}{n+1}.
	\label{lemma-2}
\end{equation}
We use \eqref{lemma-1}:
\begin{equation}
	\begin{split}
		\sum\limits_{k=0}^n \frac{1}{k+1}  \binom{n}{k} (-1)^k &= \sum\limits_{k=0}^n \frac{1}{n+1}\binom{n+1}{k+1} (-1)^k \\
		&= -\frac{1}{n+1}\sum\limits_{k=1}^{n+1} \binom{n+1}{k} (-1)(-1)^{k} \\
		&= -\frac{1}{n+1}\left(\sum\limits_{k=0}^{n+1} \binom{n+1}{k} (-1)^k - \binom{n+1}{0}(-1)^0 \right) \\
		&= -\frac{1}{n+1}\left(0 - 1 \right) \\
		&= \frac{1}{n+1}.
	\end{split}
\end{equation}
We now use induction to prove our main claim.
Assume inductively that
\begin{equation}
	\sum\limits_{k=1}^n \frac{1}{k} = -\sum\limits_{k=1}^n \frac{1}{k}\binom{n}{k}(-1)^k.
\end{equation}
Then we wish to show that
\begin{equation}
	\sum\limits_{k=1}^{n+1} \frac{1}{k} = -\sum\limits_{k=1}^{n+1} \frac{1}{k}\binom{n+1}{k}(-1)^k.
\end{equation}
We have
\begin{equation}
	\begin{split}
		-\sum\limits_{k=1}^{n+1} \frac{1}{k}\binom{n+1}{k}(-1)^k &= -\sum\limits_{k=1}^{n} \frac{1}{k}\binom{n+1}{k}(-1)^k - \frac{1}{n+1}\binom{n+1}{n+1}(-1)^{n+1} \\
		&= -\sum\limits_{k=1}^{n} \frac{1}{k}\binom{n+1}{k}(-1)^k + \frac{1}{n+1}(-1)^{n}.
	\end{split}
\end{equation}
Using a standard identity of binomial coefficients
\begin{equation}
	\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}
\end{equation}
(a recurrence relation that is the defining feature of Pascal's triangle) yields
\begin{equation}
	\begin{split}
		&\frac{1}{n+1}(-1)^{n} - \sum\limits_{k=1}^{n} \binom{n}{k}\frac{1}{k}(-1)^k - \sum\limits_{k=1}^{n} \binom{n}{k-1}\frac{1}{k}(-1)^k \\
		&\qquad = \frac{1}{n+1}(-1)^{n} - \sum\limits_{k=1}^{n} \binom{n}{k}\frac{1}{k}(-1)^k + \sum\limits_{k=0}^{n-1} \binom{n}{k}\frac{1}{k+1}(-1)^k \\
		&\qquad = \frac{1}{n+1}(-1)^{n} - \sum\limits_{k=1}^{n} \binom{n}{k}\frac{1}{k}(-1)^k + \sum\limits_{k=0}^{n} \binom{n}{k}\frac{1}{k+1}(-1)^k - \binom{n}{n}\frac{1}{n+1}(-1)^n.
	\end{split}
\end{equation}
Applying \eqref{lemma-2} yields
\begin{equation}
	- \sum\limits_{k=1}^{n} \binom{n}{k}\frac{1}{k}(-1)^k + \frac{1}{n+1}.
\end{equation}
By the inductive hypothesis, we have
\begin{equation}
	- \sum\limits_{k=1}^{n} \binom{n}{k}\frac{1}{k}(-1)^k + \frac{1}{n+1} = \sum\limits_{k=1}^n \frac{1}{k} + \frac{1}{n+1} = \sum\limits_{k=1}^{n+1} \frac{1}{k},
\end{equation}
which closes the induction.