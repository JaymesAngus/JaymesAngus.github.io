---
layout: text-page
title: Ambipolar Diffusion
---
<script id="MathJax-script" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
# ambipolar diffusion

THIS PAGE IS A PROOF OF CONCEPT FOR MY OBSIDIAN NOTES! Links will not work.

Magnetic fields can restrict the gravitational collapse of a [Molecular Clouds](molecular cloud) as charged ions are tied to magnetic field lines through the [[Lorentz Force]]. Particles become ionised through irradiation from nearby hot stars or the galactic background UV field, but the extinction effect of molecular clouds limits this effect and results in the ionisation fraction being very low. Although ions are tied to the field lines, neutral particles are not and so they can "slip" through the field lines.

Start with the [Induction Equation] for the ions, in which we can neglect classical diffusion (probably because the [Magnetic Reynolds Number] is high?)

$$\frac{\partial B}{\partial t} + \underline \nabla \times (\underline B \times \underline u_i) = 0$$

Now we can rewrite the induction equation for neutrals in terms of the [[Magnetic Support for Virial Stability#^de2ec1|drift and ion velocities]]:

$$\frac{\partial B}{\partial t} + \underline \nabla \times (\underline B \times \underline (u_i - u_d)) = 0$$

$$= \frac{\partial B}{\partial t} + \underline \nabla \times (\underline B \times \underline u_i) - \underline \nabla \times (\underline B \times \underline u_d)$$

$$=\underline \nabla \times (\underline B \times \underline u_d) = \underline \nabla \times (\frac{B}{\mu_0 \rho_n \rho_i \gamma} \times (\underline B \times (\underline \nabla \times \underline B)))$$

$$ \Rightarrow \frac{\partial B}{\partial t} + \underline \nabla \times (\underline B \times \underline u_n)\sim (\frac{B^2}{\mu_0 \rho_n}\frac{1}{\rho_i \gamma})\nabla^2 B$$

Woah! That's a diffusion term!

$$D \sim u_A^2 t_{ni}$$

Therefore the ambipolar diffusion acts on a timescale of

$$\tau_{AD} \sim \frac{R^2}{D} \sim \frac{R}{u_d}$$

Where as the dynamical timescale is

$$\tau_{dyn} \sim \frac{R}{u_A}$$

So for typical cloud parameters, the ambipolar diffusion timescale is greater by a factor of about eight.

The implication is that the magnetic field can support the cloud for a timescale greater than the dynamical timescale, but over time the field lines will escape and the cloud will be unstable to collapse.