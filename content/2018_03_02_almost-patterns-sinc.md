---
title: Almost There I
subtitle: The Pattern That Sincs Eventually 
date: 2 March 2018
category: math
tags: fun
slug: almost-patterns-sinc
---

Mathematics students are often told not to carelessly extrapolate small sample sizes into general claims.
Indeed, this is a general truth of life: isolated examples do not constitute general proof.
Say you wanted to convince me of a fact about numbers.
You could show me that your fact was true for all numbers up to ten, a hundred, a million, or to whatever ridiculously huge number you could think of---but it wouldn't constitute a mathematical proof.

This post will hopefully be the first in a series called ``Almost There.''
I will share interesting patterns that, although they seem to *surely* continue, break down eventually.

You may have noticed that I spelled "sink" incorrectly in the title.
Sharp eye.
That's because today, we'll investigate the $\mathrm{sinc}$ function:
\begin{equation}
	\mathrm{sinc}\, x =
	\begin{cases}
		\frac{\sin x}{x} & \text{if}\ x \neq 0 \\
		1 & \text{if}\ x = 0
	\end{cases}
\end{equation}
It looks like this:
![The graph of $\mathrm{sinc}\,x$. Note that at $x = 0$, this function is defined to be equal to 1.](https://gautammanohar.com/figures/sinc.png){ width=50% }

This function famously has no elementary antiderivative, yet its definite integral over the real line evaluates to
\begin{equation}
	\int_{-\infty}^\infty \mathrm{sinc}\, x \d x = \pi.
\end{equation}
Stay tuned for a proof of this fact.

A great tool for playing around with computations in math (and, thanks to the wonders of technology, a lot more) is [Wolfram Alpha](https://www.wolframalpha.com/).
We can compute some pretty complicated integrals with it, like
\begin{equation}
	\int_{-\infty}^\infty \mathrm{sinc}\, x\,\mathrm{sinc}\, \frac{x}{3} \d x = \pi,
\end{equation}
and
\begin{equation}
	\int_{-\infty}^\infty \mathrm{sinc}\, x\,\mathrm{sinc}\, \frac{x}{3}\,\mathrm{sinc}\, \frac{x}{5} \d x = \pi.
\end{equation}
Even as we multiply the integrand by another $\mathrm{sinc}$ function, the value of the definite integral remains constant at $\pi$.
The pattern continues for quite a while.
In fact,
\begin{equation}
	\int_{-\infty}^\infty \frac{\sin x}{x}\frac{\sin \frac{x}{3}}{\frac{x}{3}}\frac{\sin \frac{x}{5}}{\frac{x}{5}}\cdots\frac{\sin \frac{x}{13}}{\frac{x}{13}} \d x = \pi.
\end{equation}
But with one more term, the pattern fails spectacularly:
\begin{equation}
	\int_{-\infty}^\infty \frac{\sin x}{x}\frac{\sin \frac{x}{3}}{\frac{x}{3}}\frac{\sin \frac{x}{5}}{\frac{x}{5}}\cdots\frac{\sin \frac{x}{15}}{\frac{x}{15}} \d x = \frac{467807924713440738696537864469}{467807924720320453655260875000}\pi.
\end{equation}
This value is $4.62 \times 10^{-11}$ less than $\pi$.

What happened?
After some research, I found that such integrals were documented in [this paper](https://carma.newcastle.edu.au/jon/sinc-sums.pdf).
It turns out that, in general, for real numbers $a_1,\ldots,a_n$,
\begin{equation}
	\int_{-\infty}^\infty \prod_{k=1}^n \mathrm{sinc}\, a_kx \d x
\end{equation}
evaluates to $\pi$ if $\sum_k a_k \le 2$.
In particular, $1 + \frac{1}{3} + \cdots + \frac{1}{13} = \frac{88069}{45045} = 2 - \frac{2021}{45045}$, but adding $\frac{1}{15}$ pushes it over the edge.
So we can construct sequences of numbers $a_k$ such that the pattern holds for arbitrarily many terms before failing.
For example, the series $1 + \frac{1}{2} + \frac{1}{4} + \cdots$ famously converges to $2$, so if we set $a_k$ to be the reciprocal powers of two, the corresponding integral will be equal to $\pi$... forever.

But not all patterns hold forever---certainly not this one!