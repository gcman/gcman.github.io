---
title: Almost There I
subtitle: The Pattern That Sincs Eventually 
date: 2 March 2018
category: math
tags: fun
slug: almost-patterns-sinc
status: draft
---

Mathematics students are often told not to carelessly extrapolate small sample sizes into general claims.
Indeed, this is a general truth of life: isolated examples do not constitute general proof.
Say you wanted to convince me of a fact about numbers.
You could show me that your fact was true for all numbers up to ten, a hundred, a million, or to whatever ridiculously huge number you could think of---but it wouldn't constitute a mathematical proof.

This post will hopefully be the first in a series called ``Almost There.''
I will share interesting patterns that entice you assume that *surely* it continues forever yet eventually break down.

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
This function famously has no elementary antiderivative, yet its definite integral over the real line evaluates to
\begin{equation}
	\int_{-\infty}^\infty \frac{\sin x}{x} \d x = \pi.
\end{equation}
Stay tuned for a proof of this fact.

A great tool for playing around with computations in math (and, thanks to the recent developments in AI, a lot more) is [Wolfram Alpha](https://www.wolframalpha.com/).
We can compute some pretty complicated integrals with it, like
\begin{equation}
	\int_{-\infty}^\infty \frac{\sin x}{x}\frac{\sin \frac{x}{3}}{\frac{x}{3}} \d x = \pi,
\end{equation}
and
\begin{equation}
	\int_{-\infty}^\infty \frac{\sin x}{x}\frac{\sin \frac{x}{3}}{\frac{x}{3}}\frac{\sin \frac{x}{5}}{\frac{x}{5}} \d x = \pi.
\end{equation}
Even as we multiply the integrand by another $\mathrm{sinc}$ function, the value of the definite integral remains constant at $\pi$.
The pattern continues for quite a while.
In fact,
\begin{equation}
	\int_{-\infty}^\infty \frac{\sin x}{x}\frac{\sin \frac{x}{3}}{\frac{x}{3}}\frac{\sin \frac{x}{5}}{\frac{x}{5}}\cdots\frac{\sin \frac{x}{13}}{\frac{x}{13}} = \pi
\end{equation}