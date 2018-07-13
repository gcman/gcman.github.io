title: Relatively Prime, Relatively Often
date: 17 April 2018
category: math
tags: proof
slug: coprime-prob
summary: We derive the probability that two random integers are coprime.

Say you choose two integers.
What's the chance that they're coprime?
My intuition says that it can't be more than one-half, because half of all numbers share a factor of 2.
But I'm thoroughly wrong here.
The probability is actually $\frac{6}{\pi^2}$, which is about $61\%$.

We wish to find the probability that two randomly selected integers $m$ and $n$ are coprime.
If this is true, then $\mathrm{gcd}(m,n) = 1$.
Let's say that $p = \mathrm{P}(\mathrm{gcd}(m,n)=1)$.

Consider $p_k = \mathrm{P}(\mathrm{gcd}(a,b)=k)$ for some positive integer $k$.
For this to be true, $k$ must divide both $a$ and $b$, and $\frac{a}{k}$ and $\frac{b}{k}$ must be coprime.
And so $p_k = \mathrm{P}(k|a\,\text{and}\,k|b)\cdot\mathrm{P}\left(\mathrm{gcd}\left(\frac{a}{k},\frac{b}{k}\right)\right)$.
One in every $k$ integers is divisible by $k$.
So the first probability, namely that two random integers are both divisible by $k$, is $\frac{1}{k^2}$.
The second probability is just $p$---because $a$ and $b$ were random, so are $\frac{a}{k}$ and $\frac{b}{k}$.
And so $p_k = \frac{p}{k^2}$

Two numbers must have some greatest common divisor.
And so the sum of $p_k$ over all $k$ must be 1.
That is,
\begin{equation}
	\begin{split}
		\sum\limits_{k=1}^\infty \frac{p}{k^2} &= 1 \\
		p &= \frac{1}{\sum\limits_{k=1}^\infty \frac{1}{k^2}}.
	\end{split}
\end{equation}
The denominator is famously equal to $\frac{\pi^2}{6}$, as shown by Euler.
And so we conclude that $p = \frac{6}{\pi^2}$.