---
title: Generalising Heron's Formula to Quadrilaterals
subtitle: Deriving Brahmagupta's Formula
date: 4 February 2018
category: math
tags: geometry, proof
slug: herons-formula
---

A well-known fact in Euclidean geometry is the following expression for the area of a triangle given its side lengths:
\begin{equation}
	A = \sqrt{s(s-a)(s-b)(s-c)},
\end{equation}
where $s$ is the semiperimeter of the triangle, $\frac{a+b+c}{2}$.
Our goal is to generalize this formula to quadrilaterals.
Just like in proofs of Heron's formula that use trigonometry, we will use the formula for the area of a triangle
\begin{equation}
	A = \frac{1}{2}ab\sin C
\end{equation}
and the cosine law.
Our strategy will be to square these expressions and use the Pythagorean trigonometric identity.
Consider a quadrilateral $ABCD$ with side lengths $a,b,c,d$.

![**Figure 1.** Constructing our quadrilateral.]({filename}/figures/herons-quadrilateral.jpg){ width=50% }

Then its area is the sum of the areas of the triangles $ABD$ and $BCD$.
Let $A$ denote the area of quadrilateral $ABCD$.
Then
\begin{equation}
	\begin{split}
		A &= \text{Area}_{\triangle ABD} + \text{Area}_{\triangle BCD} \\
		A &= \frac{1}{2}ad\sin\alpha + \frac{1}{2}bc\sin\beta \\
		2A &= ad\sin\alpha + bc\sin\beta \\
		4A^2 &= a^2d^2\sin^2\alpha + b^2c^2\sin^2\beta.
	\end{split}
	\label{sin}
\end{equation}
Using the cosine law on triangles $ABD$ and $BCD$, we obtain two expressions for the square of the length of line segment $BD$:
\begin{equation}
	BD^2 = a^2 + d^2 - 2ad\cos\alpha
	\label{abd-cos}
\end{equation}
and
\begin{equation}
	BD^2 = b^2 + c^2 - 2bc\cos\beta.
	\label{bcd-cos}
\end{equation}
We equate the right sides of \eqref{abd-cos} and \eqref{bcd-cos} to obtain
\begin{equation}
	\begin{split}
		a^2 + d^2  - 2ad\cos\alpha &= b^2 + c^2 - 2bc\cos\beta \\
		a^2 + d^2 - b^2 - c^2 &= 2ad\cos\alpha - 2bc\cos\beta \\
		\frac{a^2 + d^2 - b^2 - c^2}{2} &= ad\cos\alpha - bc\cos\beta \\
		\frac{(a^2 + d^2 - b^2 - c^2)^2}{4} &= a^2d^2\cos^2\alpha + b^2c^2\cos^2\beta - 2abcd\cos\alpha\cos\beta.
	\end{split}
	\label{cos}
\end{equation}
We add \eqref{sin} and \eqref{cos}:
\begin{equation}
	\begin{split}
		4A^2 + \frac{(a^2 + d^2 - b^2 - c^2)^2}{4} &= a^2d^2\sin^2\alpha + b^2c^2\sin^2\beta + a^2d^2\cos^2\alpha + b^2c^2\cos^2\beta - 2abcd\cos\alpha\cos\beta \\
		&= a^2d^2 + b^2c^2 - 2abcd\cos\alpha\cos\beta \\
		&= (ad + bc)^2 - 2abcd - 2abcd\cos\alpha\cos\beta \\
		&= (ad + bc)^2 - 2abcd(1 + \cos\alpha\cos\beta) \\
		&= (ad + bc)^2 - 4abcd\left(\frac{1 + \cos\alpha\cos\beta}{2}\right).
	\end{split}
\end{equation}
Using the cosine double angle formula, we have
\begin{equation}
	\begin{split}
		\cos2\theta &= \cos^2\theta - \sin^2\theta \\
		\cos2\theta &= 2\cos^2\theta - 1 \\
		1 + \cos2\theta &= 2\cos^2\theta \\
		\frac{1 + \cos2\theta}{2} &= \cos^2\theta \\
		\frac{1 + \cos\theta}{2} &= \cos^2\frac{\theta}{2}.
	\end{split}
\end{equation}
We can substitute this into our equation for $4A^2$ to continue:
\begin{equation}
	\begin{split}
		4A^2 &= (ad + bc)^2 - 4abcd\cos^2\frac{\alpha + \beta}{2} - \frac{(a^2 + d^2 - b^2 - c^2)^2}{4} \\
		16A^2 &= 4(ad + bc)^2 - (a^2 + d^2 - b^2 - c^2)^2 - 16abcd\cos^2\frac{\alpha + \beta}{2} \\
		16A^2 &= (2ad+2bc + a^2 + d^2 - b^2 - c^2)(2ad+2bc - a^2 - d^2 + b^2 + c^2) - 16abcd\cos^2\frac{\alpha + \beta}{2} \\
		16A^2 &= ((a+d)^2 - (b-c)^2)((b+c)^2 - (a-d)^2) - 16abcd\cos^2\frac{\alpha + \beta}{2} \\
		16A^2 &= (-a+b+c+d)(a-b+c+d)(a+b-c+d)(a+b+c-d) - 16abcd\cos^2\frac{\alpha + \beta}{2} \\
		16A^2 &= 16\left(\frac{-a+b+c+d}{2}\right)\left(\frac{a-b+c+d}{2}\right)\left(\frac{a+b-c+d}{2}\right)\left(\frac{a+b+c-d}{2}\right) - 16abcd\cos^2\frac{\alpha + \beta}{2}.
	\end{split}
\end{equation}
We introduce $s = \frac{a+b+c+d}{2}$, the semiperimeter of the quadrilateral.
\begin{equation}
	\begin{split}
		16A^2 &= 16(s-a)(s-b)(s-c)(s-d) - 16abcd\cos^2\frac{\alpha + \beta}{2} \\
		A &= \sqrt{(s-a)(s-b)(s-c)(s-d) - abcd\cos^2\frac{\alpha + \beta}{2}}.
	\end{split}
\end{equation}
And we have a formula for the area of an arbitrary quadrilateral given its side lengths (this formula is called Bramhagupta's formula).

It looks an awful lot like Heron's formula; it just has a pesky $-abcd\cos^2\frac{\alpha + \beta}{2}$ term.
Let's try getting rid of that term, which would maximize the area of the quadrilateral.
We want $\cos^2\frac{\alpha + \beta}{2}$ to be $0$, so we set $\alpha + \beta = \pi$.
This is true if the quadrilateral is cyclic.
And so we have discovered that, given four side lengths, we can form the quadrilateral with the maximum area if we arrange the lengths such that opposite angles are supplementary (if we make a cyclic quadrilateral).