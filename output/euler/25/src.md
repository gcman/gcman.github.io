---
title: Problem 25 - 1000-digit Fibonacci Number
date: 12 June 2018
category: euler
tags: proof
slug: euler/25
problem: 25
summary: My solution to problem 25 of Project Euler.
---

# Problem Statement

What is the first term in the Fibonacci sequence to contain $N$ digits?

# My Algorithm

We will use Binet's formula for the $n$-th fibonacci number
\begin{equation}
	F_n = \frac{\varphi^n - (-\varphi)^{-n}}{\sqrt{5}}.
\end{equation}
The $(-\varphi)^{-n}$ quickly becomes negligible.
So we can make the approximation
\begin{equation}
	F_n \approx \frac{\varphi^n}{\sqrt{5}}.
	\label{approx}
\end{equation}

A number $n$ has $\lfloor \log_{10} n \rfloor + 1$ digits.
So we must solve the following equation such that $n$ is minimized:
\begin{equation}
	\lfloor \log_{10} F_n \rfloor + 1 = N.
	\label{fib-eq}
\end{equation}
Recall that $\lfloor x \rfloor$ is defined as the greatest integer less or equal to than $x$.
That is,
\begin{equation}
	x \le \lfloor x \rfloor < x + 1.
	\label{floor}
\end{equation}
Applying \eqref{approx} and \eqref{floor} to \eqref{fib-eq} gives
\begin{equation}
	\begin{split}
		N &\le 1 + \log_{10} F_n < N + 1 \\
		N - 1 & \le \log_{10} \frac{\varphi^n}{\sqrt{5}} \\
		N - 1 + \frac{\log_{10}5}{2} &\le n \log_{10} \varphi \\
		\frac{N - 1 + \frac{\log_{10}5}{2}}{\log_{10}\varphi} &\le n.
	\end{split}
	\label{final}
\end{equation}

We see that $n$ is minimized when it is the smallest integer greater than the left side of \eqref{final}.
This is precisely the definition of the ceiling function.
And so we have our desired answer:
\begin{equation}
	n = \left\lceil \frac{N - 1 + \frac{\log_{10}5}{2}}{\log_{10}\varphi} \right\rceil.
\end{equation}
Because our solution is just a computation, it has time complexity $O(1)$.
In our code, we just need to handle the corner case where $N = 1$; here our approximation \eqref{approx} introduces enough error to return an incorrect answer.