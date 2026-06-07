---
layout: text-page
title: Random Sampling From PDFs
---
<script id="MathJax-script" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
# random sampling from PDFs

How to sample random variables from an underlying probability density function. Analytical and numerical
approaches.

## Analytical method
To select a random variable, $$X$$ from a probability density function, $$p(x)$$, we
must first normalise it over all possible values that our
variable could take. We'll call this range $$[a, b]$$. Next we integrate $$p(x)$$ over the
range $$[a, X]$$ to compute the cumulative distribution function (CDF). We
then invert the function for the CDF and substitute in the value of a
uniformly distributed random variable, $$\xi$$. The resulting figure is a
value for $$X$$ sampled from the original PDF!

Eg. sample a value of $$X$$
from a PDF $$p(x)$$, where $$X$$ can take any value from $$a$$ to $$b$$:

$$p(x) = p(x) / \int_a^b p(x)dx$$

$$F(x) = \int_a^X p(x)$$

$$X = F^{-1}(\xi)$$

## Numerical (rejection) method
When the CDF cannot be inverted as described
above, we use the rejection method to sample from a PDF. First, pick a
random $$x$$ value in the range $$[a, b]$$ using $$x_1 = a + \xi (b-a)$$, then
use it to compute $$P(x_1)$$. Now pick a random $$y$$ value in the range $$[0,
P_{max}]$$.

If $$y_1 > P(x_1)$$, reject $$x_1$$.
Keep picking random values of
$$x$$ and $$y$$ until $$y_i \leq P(x_1)$$, then accept $$x_i$$. The efficiency of
this method is equal to the area under $$p(x)$$.