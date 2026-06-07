---
layout: text-page
title: Simulating the Lightcurve
---
<script id="MathJax-script" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>

# Simulating the Light Curve

The initial requirement for this project was to develop code which would simulate the light curve of a gravitational microlensing event.
For a point-source-point-lens model, the magnification $$A$$ can be exactly described by a quadratic in terms of $$u$$, the impact parameter
in units of the [Einstein radius](/projects/mphys-dissertation//microlensing-glossary.html).

The Einstein radius is a characteristic scale in microlensing, defined as

$$\theta_E = \left (\frac{4GM}{D_{rel}c^2} \right )^{1/2}$$

In the case that the impact parameter
$$u$$ is zero, the source image is deflected to a circle with a radius equivalent to the Einstein radius.

$$A(u) = \frac{u^2 + 2}{u\sqrt{u^2 + 4}}$$

Add a second body to the lens system, and a fifth-order complex polynomial must be solved to describe the resulting time-series magnification. No analytical
solution is possible for fifth order polynomials, and so this requires a significant degree of numerical computation.

After one week of trying to write this simulation from scratch and becoming increasingly conscious of the twelve week project timeframe, I opted to use the existing Python package

*MulensModel*: a Python package that utilises contour integration methods to rapidly determine the expected magnification of a given microlensing event. A game-changer considering the
high volume of parameters that I intended to experiment with. MulensModel also provides a trajectory map for your specified event
which allows the user to visually determine which planetary configurations should result in a detectable perturbation.