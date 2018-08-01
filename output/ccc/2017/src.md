---
title: Unofficial CCC 2017 Solutions
date: 30 March 2018
category: chemistry
tags: contest
slug: ccc/2017
summary: Unofficial full solutions and explanations to Part C of the 2017 Canadian Chemistry Contest/Olympiad.
---

This is part of a [project](../) to provide unofficial solutions for part C of the [Canadian Chemistry Contest](http://www.cheminst.ca/outreach/canadian-chemistry-contest).
You can find the 2017 contest [here](problems.pdf).

# General Chemistry

## Part A

Following the standard procedure to draw Lewis structures, we first note that sulfur, being more electronegative than oxygen, will be the central atom.
Next, we count valence electrons: sulfur and oxygen are in the same group and both have six valence electrons.
Sulfur dioxide is neutral, so we know there are 18 electrons to distribute.
Now we can place lone pairs: each oxygen is bonded to the sulfur, which uses four electrons (two in each bond).
We initially place the 14 remaining electrons as seven lone pairs---three on each oxygen (the maximum possible) and the last on sulfur.

![The incomplete Lewis structure of sulfur dioxide.](/home/gautam/Documents/Website/content/figures/so2-incomplete.pdf){ width=20% }

In this part, we do not want sulfur to have an expanded octet.
Right now, the sulfur atom only has six electrons around it.
To satisfy its octet, we take a lone pair on one of the oxygen atoms and make it a sulfur-oxygen bond.
But both oxygen atoms work equally well, which gives us the two resonance forms we were looking for.
We conclude by adding formal charges and drawing a double-headed resonance arrow.

![The resonance structures of sulfur dioxide that do not use sulfur's expanded octet. These are commonly accepted as the resonance forms with the greatest contribution.](/home/gautam/Documents/Website/content/figures/so2-resonance.pdf){ width=60% }

## Part B

We simply take one of the lone pairs on the oxygen with a negative formal charge in one of the resonance structures from the first part and make it a sulfur-oxygen bond.
Note that this is only possible if sulfur uses its expanded octet and becomes pentavalent (four bonds and one lone pair).

![A resonance form of sulfur dioxide with no formal charges.](/home/gautam/Documents/Website/content/figures/so2-expanded-octet.pdf){ width=20% }

## Part C

Sulfur forms sigma-bonds with oxygen, which require $\mathrm{sp}^2$ or $\mathrm{sp}$ hybridization.
There are no triple bonds, so the sulfur atom must be $\mathrm{sp}^2$ hybridized.

## Part D

Sulfur has two sigma bonds and pi bonds to the more electronegative oxygen, so it is electron deficient and can act as a Lewis acid.
Since we are not given much information about the products of the reaction, we can safely assume an adduct is formed.
Then we have
\begin{equation}
	\ce{SO2 + A -> A*SO2}
\end{equation}
For example, the Lewis base could be water, whose oxygen lone pair attacks the central sulfur atom to form sulfurous acid, $\ce{H2SO3}$.

## Part E

Sulfur has a lone pair that can donate electrons, acting as a Lewis base.
By similar reasoning to the previous part, we have
\begin{equation}
	\ce{SO2 + B -> SO2*B}
\end{equation}
For example, the Lewis acid could be borane, $\ce{BH3}$, which is even more electron deficient than sulfur dioxide and could capture it.

# Physical Chemistry

For this problem, we shall use the values for Planck's constant $h = 6.62608 \times 10^{-34}\,\mathrm{J}\,\mathrm{s}$ and the mass of the electron $m = 9.10939 \times 10^{-31}\,\mathrm{kg}$.

## Part A

We are given $n = 2$ and $L = 1 \times 10^{-9} \,\mathrm{m}$, from which we can simply apply the given equation:
\begin{equation}
	\begin{split}
		E &= n^2\frac{h^2}{8mL^2} \\
		&= 2^2\frac{(6.62608 \times 10^{-34})^2}{8(9.10939 \times 10^{-31})(1 \times 10^{-9})^2} \\
		&= 2.40987 \times 10^{-19} \,\mathrm{J} \\
		&\approx 2.41 \times 10^{-19} \,\mathrm{J}.
	\end{split}
\end{equation}
We report our final answer to three significant figures.

## Part B

By definition, the phenyl groups are not part of the linear conjugated system.
All the pi bonds are separated by exactly one sigma bond, so they are all conjugated.
There are four pi bonds, each of which is composed of two electrons, so there are eight pi electrons in the conjugated system.

## Part C

The four pi bonds in this molecule are composed of two p orbitals each.
These eight atomic orbitals combine to form eight molecular orbitals of increasing energy.
Four of them are bonding orbitals, and four antibonding.
In the ground state, no electrons occupy the higher energy antibonding orbitals, so the pi electrons occupy four orbitals

## Part D

If there are $N$ pi electrons, then there are $\frac{N}{2}$ occupied orbitals of increasing energy.
Then an electron in the highest of these has energy
\begin{equation}
	\begin{split}
		E &= n^2\frac{h^2}{8mL^2} \\
		&= \left(\frac{N}{2}\right)^2\frac{h^2}{8mL^2} \\
		&= \frac{N^2h^2}{32mL^2}.
	\end{split}
	\label{homo}
\end{equation}

## Part E

The lowest unoccupied molecular orbital is one energy level higher than the highest occupied molecular orbital, by definition.
Then, applying our reasoning from the previous part, an electron in the LUMO has energy
\begin{equation}
	\begin{split}
		E &= n^2\frac{h^2}{8mL^2} \\
		&= \left(\frac{N}{2} + 1\right)^2\frac{h^2}{8mL^2} \\
		&= \left(\frac{N+2}{2}\right)^2\frac{h^2}{8mL^2} \\
		&= \frac{(N+2)^2h^2}{32mL^2}.
	\end{split}
	\label{lumo}
\end{equation}
To find the energy difference between the LUMO and HOMO, we subtract \eqref{homo} from \eqref{lumo}:
\begin{equation}
	\begin{split}
		\Delta E &= \frac{(N+2)^2h^2}{32mL^2} - \frac{N^2h^2}{32mL^2} \\
		&= (N^2 + 4N + 4 - N^2)\frac{h^2}{32mL^2} \\
		&= \frac{(4N + 4)h^2}{32mL^2} \\
		&= \frac{(N+1)h^2}{8mL^2}.
	\end{split}
	\label{homo-lumo-diff}
\end{equation}

## Part F

Every pi bond separated from another pi bond by exactly one sigma bond and every sigma bond in between two pi bonds in retinal is part of the linear conjugated system.
Then we have five carbon-carbon pi bonds and five carbon-carbon sigma bonds, as well as one carbon-oxygen pi bond in the system.
We can assume that the given length for carbon-carbon bonds is an average across single and double bonds.
We then estimate $L$ using the given values:
\begin{equation}
	\begin{split}
		L &= 10\cdot0.140\,\mathrm{nm} + 0.123\,\mathrm{nm} \\
		&= 1.400 + 0.123 \\
		&= 1.523\,\mathrm{nm}.
	\end{split}
	\label{retinal}
\end{equation}

## Part G

From our observations in the previous part, $N = 12$, because there are six pi bonds, each with two electrons, in the system.
If retinal reaches an excited state, then an electron is promoted from the HOMO to the LUMO.
Then we can use our estimated value for $L$ from \eqref{retinal} and apply equation \eqref{homo-lumo-diff}:
\begin{equation}
	\begin{split}
		\Delta E &= \frac{(N+1)h^2}{8mL^2} \\
		&= \frac{13(6.62608 \times 10^{-34})^2}{8(9.10939 \times 10^{-31})(1.523 \times 10^{-9})^2} \\
		&= 5.142525 \times 10^{-28} \,\mathrm{J}.
	\end{split}
	\label{ret-e}
\end{equation}

From the universal wave equation, we know $E = h\nu$, and we know $\nu = \frac{c}{\lambda}$, so we have $E = \frac{hc}{\lambda}$.
Applying \eqref{ret-e}, we have
\begin{equation}
	\begin{split}
		E &= \frac{hc}{\lambda} \\
		\lambda &= \frac{hc}{E} \\
		&= \frac{(6.62608 \times 10^{-34})(2.997925 \times 10^8)}{5.142525 \times 10^{-28}} \\
		&= 3.8597 \times 10^{-7}
	\end{split}
\end{equation}
Reporting our answer to four significant figures (the limiting value is $L$), we find that the wavelength of the light absorbed by retinal to reach an excited state is $356.0 \,\mathrm{nm}$.

# Inorganic Chemistry

## Part A

Applying the Aufbau principle, we know the $3\mathrm{d}$ orbital is higher in energy than the $4\mathrm{s}$ orbital.
From this the electron configuration follows easily: just follow the periodic table.
\begin{equation}
	1\mathrm{s}^2 2\mathrm{s}^2 2\mathrm{p}^6 3\mathrm{s}^2 3\mathrm{p}^6 4\mathrm{s}^2 3\mathrm{d}^2
\end{equation}

## Part B

We note that $\ce{FeTiO3}$ must have the same coefficient of $\ce{TiCl4}$ and $\ce{FeCl3}$, which are the only titanium and iron containing compounds on the product side.
If we call this value $x$, then we see that $\ce{C}$ and $\ce{CO}$ have coefficient $3x$.
The final reagant, $\ce{Cl2}$, has coefficient $\frac{7x}{2}$.
We clear fractions by multiplying by 2 and set $x = 1$ to get the balanced equation:
\begin{equation}
	\ce{2FeTiO3(s) + 7Cl2(g) + 6C(s,\mathrm{graphite}) -> 2TiCl4(l) + 2FeCl3(s) + 6CO(g)}
\end{equation}

## Part C

Titanium tetrachloride violently hydrolyzes to form titanium dioxide and hydrochloric acid as follows:
\begin{equation}
	\ce{TiCl4(l) + 2H2O(g) -> TiO2(s) + 4HCl(aq)}
\end{equation}

## Part D

Examination of the diagram shows that each oxygen atom has three titanium atoms around it with $120^\circ$ bond angle.
Furthermore, each titanium atom has six oxygen atoms around it with $90^\circ$ angle.
This means that oxygen has local trigonal planar geometry, and titanium local octahedral geometry.

## Part E

We know density is mass over volume, so we will find the unit mass and unit volume.

In the unit cell, there are one corner titanium atoms, which each contribute one-eighth of an atom, and one full titanium atom.
Furthermore, there are four oxygen atoms and two face oxygen atoms, which each contribute one-half of an atom.
This gives two titanium and five oxygen atoms in the unit cell.
These elements have molar masses $m_{\ce{Ti}} = 47.87 \,\mathrm{g}\,\mathrm{mol}^{-1}$ and $m_{\ce{O}} = 16.00 \,\mathrm{g}\,\mathrm{mol}^{-1}$.
This means the unit mass is
\begin{equation}
	\frac{2\cdot47.87 + 5 \cdot 16.00}{6.022\times10^{23}} = 2.918 \times 10^{-22} \,\mathrm{g}.
	\label{mass}
\end{equation}

The unit volume is
\begin{equation}
	abc = 0.4584^2(0.2953) = 0.06205 \,\mathrm{nm}^3 = 6.205 \times 10^{-23} \,\mathrm{cm}^3.
	\label{volume}
\end{equation}

From \eqref{mass} and \eqref{volume}, we get the density:
\begin{equation}
	\rho_{\ce{TiCl}} = \frac{2.918 \times 10^{-22}}{6.205 \times 10^{-23}} = 4.703 \,\mathrm{g}\,\mathrm{cm}^{-3}.
\end{equation}

## Part F

We are given $\Delta H_\text{vap} = 37500 \,\mathrm{J}\,\mathrm{mol}^{-1}$.
Under the conditions of SATP, $T_1 = 298\,\mathrm{K}$.
We set $P_1 = 1.70 = 101.70 \,\mathrm{kPa}$.
By definition, $P_2$, or the vapour pressure at boiling point is one atmosphere, or $101.325 \,\mathrm{kPa}$.
We use the gas constant $R = 8.31451 \,\mathrm{J}\,\mathrm{K}^{-1}\,\mathrm{mol}^{-1}$.
We then solve for the boiling point, $T_2$, reported to three significant figures:
\begin{equation}
	\begin{split}
		\ln\frac{P_1}{P_2} &= \frac{\Delta H_\text{vap}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) \\
		\frac{1}{T_2} &= \frac{R}{\Delta H_\text{vap}}\ln\frac{P_1}{P_2} + \frac{1}{T_1} \\
		T_2 &= \left(\frac{R}{\Delta H_\text{vap}}\ln\frac{P_1}{P_2} + \frac{1}{T_1}\right)^{-1} \\
		&= \left(\frac{8.31451}{37500}\ln\frac{1.70}{101.325} + \frac{1}{298}\right) \\
		&= 408 \,\mathrm{K}.
	\end{split}
\end{equation}

## Part G

Titanium tetrachloride gas could be bubbled into a vat of liquid magnesium metal, upon which it would be reduced.
Solid titanium would be produced and, being denser than magnesium, sink to the bottom where it could be collected.
Titanium would be the only solid, and titanium tetrachloride would be the only gas; magnesium metal and magnesium chloride would be liquids.
The chemical equation is as follows:
\begin{equation}
	\ce{TiCl4(g) + 2Mg(l) -> 2MgCl2 + Ti(s)}
\end{equation}

# Organic Chemistry

## Parts A and B

These two parts deal with the same synthesis.
The first step adds three carbon atoms, four hydrogen atoms, and one oxygen atom.
The presence of the aryl ketone in the finished product indicates that this addition step is likely a Friedel-Crafts acylation, with propanoyl chloride and a strong Lewis acid calalyst, such as aluminum chloride.

![Reagants Q, propanoyl chloride, and R, $\ce{AlCl3}$ react with benzene in a Friedel-Crafts acylation to form intermediate S.](/home/gautam/Documents/Website/content/figures/2017-synth-1.pdf){ width=60% }

In the next step, a hydrogen atom is substituted for a chlorine atom is added meta to the acyl group, which is electron withdrawing and directs meta.
This indicates an electrophilic aromatic halogenation with chlorine gas and strong Lewis acid catalyst, again aluminum chloride.

![Catalyzed by aluminum chloride, chlorine gas substitutes to form the given intermediate V.](/home/gautam/Documents/Website/content/figures/2017-synth-2.pdf){ width=20% }

Next, the compound is subjected acidic conditions, under which the ketone oxygen is protonated and forms its enol tautomer.
After bromine adds to the alkene on the alpha carbon and the ketone is reformed after deprotonation, we obtain an alpha brominated product.

![Bromination yields intermediate W.](/home/gautam/Documents/Website/content/figures/intermediate-W.pdf){ width=25% }

We then add a nitrogen compound, which, judging from the structure of the desired product, is likely tert-butylamine.
The nucleophilic nitrogen drives an $\text{S}_\text{N}2$ reaction with bromine as the leaving group.
Now we have a bromine salt; bupropion is a chlorine salt.
To replace bromine, we add a stoichiometric amount of hydrochloric acid.

![Addition of tert-butylamine, reagant X, forms intermediate Y, which gives bupropion after treatment with reagant Z, hydrochloric acid.](/home/gautam/Documents/Website/content/figures/2017-synth-3.pdf){ width=60% }

## Part C

Bupropion has only one stereocenter (at the carbon to which the nitrogen is bonded).
And so it has two stereoisomers.

## Part D

Chlorine salts are generally soluble in water, so buproprion likely dissolves.

## Part E

In this part, we predict the products formed after intermediate V reacts with the following reagants.
We have

#. Reduction of the ketone to a secondary alcohol by sodium borohydride
#. Gringard addition on the electrophilic carbonyl carbon
#. Reduction of the aryl ketone to an alkane
#. Formation of an imine from a ketone and primary amine
#. Formation of an enamine from a ketone and secondary amine

![The structures of the products from the five sets of reagants.](/home/gautam/Documents/Website/content/figures/2017-synth-4.pdf){ width=70% }

# Analytical Chemistry

## Part A

We break this reaction into a reduction half-reaction
\begin{equation}
	\ce{Cu^{2+}(aq) + I-(aq) + e- -> CuI(s)}
\end{equation}
and an oxidation half-reaction
\begin{equation}
	\ce{2I-(aq) -> I2(aq) + 2e-}
\end{equation}
Adding the two reactions together (after multiplying the reduction reaction by 2), we have the balanced form
\begin{equation}
	\ce{2Cu^{2+}(aq) + 4I-(aq) -> 2CuI(s) + I2(aq)}
\end{equation}

## Part B

Just like in the first part, we have a reduction half-reaction
\begin{equation}
	\ce{I2(aq) + e- -> I-(aq)}
\end{equation}
and an oxidation half-reaction
\begin{equation}
	\ce{2S2O3^{2-}(aq) -> S4O6^{2-}(aq) + 2e-}
\end{equation}
Again, we balance:
\begin{equation}
	\ce{2I2(aq) + 2S2O3^{2-}(aq) -> 2I-(aq) + S4O6^{2-}(aq)}
\end{equation}

## Part C

In the first reaction, copper (II) and iodine are in a $2:1$ ratio.
In the second reaction, iodine and thiosulfate are in a $1:1$ ratio.
This means that
\begin{equation}
	n_\text{Cu} = 2n_\text{T}.
\end{equation}

## Part D

We find the moles of thiosulfate used:
\begin{equation}
	n_\text{T} = 0.1002 \cdot 0.03207 = 3.21341 \times 10^{-3}.
\end{equation}
From the previous part, we know the moles of copper (II) are half the moles of thiosulfate, so
\begin{equation}
	n_\text{Cu} = \frac{n_\text{T}}{2} = \frac{3.21341 \times 10^{-3}}{2} = 1.60671 \times 10^{-3}.
\end{equation}
We then divide by the volume of copper (II) solution
\begin{equation}
	C_\text{Cu} = \frac{n_\text{Cu}}{V_\text{Cu}} = \frac{1.60671 \times 10^{-3}}{0.050000} = 0.032134
\end{equation}
Reporting our answer to four significant figures, we find that the initial concentration of copper (II) ions was $0.03213 \,\mathrm{mol}\,\mathrm{L}^{-1}$.

## Part E

An excess of iodide ensures that all of the copper (II) ions react to form copper iodide, but in particular iodine, which we titrate with thiosulfate to find the initial concentration of copper (II).
If too little iodide is used, then the final result will underestimate the initial concentration.

## Part F

A suitable indicator for this titration is starch solution.
It adsorbs the triiodide ion, which is formed from iodine and iodide ions.
The starch-triiodide complex produces a deep blue-black colour, which becomes colourless when only iodide and no iodine, and thus no triiodide, is present in solution---this is the endpoint.
However, this complex is not very soluble in water, so it should be added once most of the iodine has reacted with thiosulfate.
You can tell when this has happened, as the brownish iodine colour will become pale.

## Part G

One possible issue is that the starch hydrolyzes under attack by acidic conditions, rendering it incapable of adsorbing triiodide and acting as an indicator.
Another possible issue is that the starch cannot adsorb enough triiodide, which can occur at high temperatures.
To remedy this, titrations involving iodine should be performed in cold, neutral conditions.
