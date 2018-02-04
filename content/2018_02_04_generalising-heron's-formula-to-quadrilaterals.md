---
title: Generalising Heron's Formula to Quadrilaterals
subtitle: Deriving Brahmagupta's Formula
date: 4 February 2018
category: math
tags: geometry, proof
slug: herons-formula
status: draft
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