title: Prime Reciprocals Diverge!
date: 20 May 2018
category: math
tags: primes,combinatorics,proof
slug: prime-reciprocals
summary: We prove that the sum of the reciprocals of the prime numbers diverges.

# Introduction

In this post, we will investigate the infinite series
\begin{equation}
	\sum_{p} \frac{1}{p},
\end{equation}
taken over all primes $p$.
In particular, we will show that this sum diverges.

# Calculus and PNT

First, we'll show that this problem falls to the incredible might of the following inequalty bounding the $n$-th prime:
\begin{equation}
	n\log n - n \log\log n \le p_n \le n\log n + n\log\log n \quad (n > 5)
\end{equation}
This identity comes in quite handy when solving computer science problems about primes, and you need to generate at least $n$ primes or something of the sort.
It's derived from the Prime Number Theorem.

Using the upper bound, we know that $\frac{1}{p} \ge \frac{1}{n\log n + n \log\log n}$ for $n > 5$.
And so
\begin{equation}
	\sum_{p} \frac{1}{p} \ge \sum\limits_{n=6}^\infty \frac{1}{n\log n + n \log\log n}.
\end{equation}
Because $\log x$ is a monotonically increasing function, $\log\log x \le \log x$ for all $x$.
And so $n\log n + n \log n \ge n\log n + n\log\log n$.
This means that
\begin{equation}
	\sum\limits_{n=6}^\infty \frac{1}{n\log n + n \log\log n} \ge \sum\limits_{n=6}^\infty \frac{1}{2n\log n}. 
\end{equation}

Here's where the calculus comes in.
Remember the integral test?
It says that if a function $f$ is non-negative, continuous, and monotonically decreasing on a certain interval $[a,b+1]$, then
\begin{equation}
	\int_a^{b+1} f(x) \d x < \sum\limits_{\substack{n \in \mathbb{Z}\\a\le n \le b}}f(n)
\end{equation}
 the sum of $f(n)$ over integers $a \le n \le b$ is greater than the integral of $f$ over that interval.
We know $x$ is increasing and continuous, as is $\log x$.
And so $x \log x$ is increasing and continuous, which means that $\frac{1}{x \log x}$ is decreasing.
On $[6,\infty)$, it's also non-negative.

This means that
\begin{equation}
	\sum_{p} \frac{1}{p} \ge \sum\limits_{n=6}^\infty \frac{1}{2n\log n} \ge \frac{1}{2} \int_6^\infty \frac{1}{x\log x} \d x.
\end{equation}
Substituting $u = \log x, \d u = \frac{1}{x} \d x$ gives
\begin{equation}
	\int_{\log 6}^\infty \frac{\d u}{u},
\end{equation}
which we evaluate as $\left[ \log u \right]_{\log_6}^\infty = \infty$.
But wait!
This means that the sum of the reciprocals of the primes is greater than infinity, which of course means that it cannot converge to any finite value.

# Combinatorics

In my opinion, this combinatorially inspired method is way cooler.

## Squares and Squarefree Products

First, every integer can be written uniquely as the product of a square and an integer which is the product of distinct primes (that is, it is squarefree).
To see this, consider the prime factorization of a number
\begin{equation}
	n = \prod_{p_i|n} p_i^{e_i},
\end{equation}
where $e_i$ is the maximum positive integer such that $p_i^{e_i}$ divides $n$.
Then for each odd $e_i$, factor out $p_i$.
Then each exponent in the product is even, which means it is a square, and the term outside the product consists of primes with exponent 1.

## Unleashing the Combo Punches

Second, each term in 
\begin{equation}
	\prod_p \left(1 + \frac{1}{p}\right)
	\label{squarefree}
\end{equation}
is formed by multiplying either $1$ or $\frac{1}{p}$ for each $p$, which means each term is the product of distinct primes.
Furthermore, because the product is over all primes, every possible combination of primes is represented here exactly once.
It is clear that
\begin{equation}
	\sum\limits_{n=1}^\infty \frac{1}{n^2}
	\label{square}
\end{equation}
contains the reciprocal of each square exactly once.
Its value is the subject of the Basel problem, which Euler famously solved: $\frac{\pi^2}{6}$.
All we really need is that the series converges to some finite value $C$.
And so the product of \eqref{squarefree} and \eqref{square} is 
\begin{equation}
	\left(\sum\limits_{n=1}^\infty \frac{1}{n^2}\right)\prod_p \left(1 + \frac{1}{p}\right) = \sum\limits_{n=1}^\infty \frac{1}{n},
	\label{harm-prod}
\end{equation}
the harmonic series.
This is because each term consists of a selection from the first sum (of reciprocals of squares) and the second sum (of reciprocals of squarefree numbers).
Because all squares and squarefree numbers are here, the reciprocal of each number is represented.
This fact is not integral to the divergence proof, but because the representation of a number as a product of a square and a squarefree number is unique, each reciprocal is represented exactly once, so the product is exactly equal to the harmonic series.
The important fact here is that the harmonic series diverges.

### The Divergence of the Harmonic Series

To see this, we can use the integral test again (with the function $\frac{1}{x}$), but we can also do it without calculus.
Suppose the harmonic series converges to some value $H$.
Then
\begin{equation}
	H = 1 + \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \cdots
\end{equation}
Because $n + 1 > n$ for all $n$, we have $\frac{1}{n + 1} < \frac{1}{n}$ for all $n$.
Replacing terms in a sum with smaller terms means the resulting sum is smaller.
So
\begin{equation}
	\begin{split}
		H &> \frac{1}{2} + \frac{1}{2} + \frac{1}{4} + 1{4} + \frac{1}{6} + \frac{1}{6} + \cdots \\
		&= 1 + \frac{1}{2} + \frac{1}{3} + \cdots \\
		&= H.
	\end{split}	
\end{equation}
We ended up with $H > H$, which is certainly not true for any finite value.
And so the harmonic series diverges.

## Finishing Touches

Third, we'll use the identity
\begin{equation}
	1 + x \le e^x.
	\label{e-ident}
\end{equation}
For three different proofs of this fact, see my article on [comparing $e^\pi$ and $\pi^e$](../e-pi/).
Applying \eqref{e-ident} to \eqref{harm-prod} gives
\begin{equation}
	\sum\limits_{n=1}^\infty \le \left(\sum\limits_{n=1}^\infty \frac{1}{n^2}\right)\prod_p \left(1 + \frac{1}{p}\right) \le C\prod_p e^{-p}.
\end{equation}
Let's use some exponent rules to clean things up.
\begin{equation}
	\begin{split}
		\sum\limits_{n=1}^\infty &\le Ce^{\sum_p \frac{1}{p}} \\
		\log \sum\limits_{n=1}^\infty &\le \log C + \sum_p \frac{1}{p}.
	\end{split}
\end{equation}
Becuase $C$ is finite, $\log C$ is also finite, and so we can see that the desired sum is greater than the harmonic series, which establishes its divergence.

# Bounding the Beast

By slightly modifying the above arguments---whenever you sum over all $p$ or all natural numbers, change the infinite sum to a partial sum over $p \le k$, for example---we obtain the following bound:
\begin{equation}
	\log\sum\limits_{n=1}^k \frac{1}{n} - \log \frac{\pi^2}{6} \le \sum\limits_{p \le k} \frac{1}{p}.
\end{equation}
We can make this even prettier by... using some calculus.
Because $\frac{1}{x}$ is decreasing and continuous, we can use the integral test to bound the partial harmonic series
\begin{equation}
	\log\sum\limits_{n=1}^k \frac{1}{n} \ge \int_1^{k+1} \frac{1}{x} \d x = \log(k+1) - \log 1 = \log(k+1).
\end{equation}
And so we obtain the very nice lower bound
\begin{equation}
	\log\log(k+1) - \log\frac{\pi^2}{6} \le \sum\limits_{p \le k} \frac{1}{p}.
\end{equation}

# Conclusion

So, calculus or combinatorics?
I think both methods are cool in their own right---one uses continuous methods to analyze prime numbers, which are discrete entities, while the other is just mind-numbingly brilliant.
Perhaps the calculus arguments are cleaner, but the combinatorics ones are much more inspiring and hide some deeper insights.