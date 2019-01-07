+++
title = "Relatively Prime, Relatively Often"
author = ["Gautam Manohar"]
description = "We derive the probability that two random integers are coprime."
date = 2018-04-17
tags = ["primes", "combinatorics"]
categories = ["math"]
draft = false
+++

Say you choose two integers. What's the chance that they're coprime? My
intuition says that it can't be more than one-half, because half of all numbers
share a factor of 2. But I'm thoroughly wrong here. The probability is actually
\\(\frac{6}{\pi^2}\\), which is about \\(61\%\\).

We wish to find the probability that two randomly selected integers \\(m\\) and \\(n\\)
are coprime. If this is true, then \\(\mathrm{gcd}(m,n) = 1\\). Let's say that \\(p =
\mathrm{P}(\mathrm{gcd}(m,n)=1)\\). Consider \\(p\_k =
\mathrm{P}(\mathrm{gcd}(a,b)=k)\\) for some positive integer \\(k\\). For this to happen, \\(k\\) must divide both \\(a\\) and \\(b\\), and \\(\frac{a}{k}\\) and \\(\frac{b}{k}\\) must
be coprime.

And so \\(p\_k =
\mathrm{P}(k|a\,\text{and}\,k|b)\cdot\mathrm{P}\left(\mathrm{gcd}\left(\frac{a}{k},\frac{b}{k}\right)
= 1\right)\\). One in every \\(k\\) integers is divisible by \\(k\\), so the first
probability is \\(\frac{1}{k^2}\\). The second probability is just $p$---because \\(a\\) and \\(b\\) were
random, so are \\(\frac{a}{k}\\) and \\(\frac{b}{k}\\). And so \\(p\_k = \frac{p}{k^2}\\).

But any two numbers have a greatest common divisor. That means the sum of \\(p\_k\\)
over all \\(k\\) covers all the possibilities, so it must be 1. That is,

\begin{equation}
\begin{split}
\sum\_{k=1}^\infty \frac{p}{k^2} &= 1 \\\\\\
p &= \left(\sum\_{k=1}^\infty \frac{1}{k^2}\right)^{-1}.
\end{split}
\end{equation}

That sum is famously equal to \\(\frac{\pi^2}{6}\\), as shown by Euler. And
so we conclude that \\(p = \frac{6}{\pi^2}\\).