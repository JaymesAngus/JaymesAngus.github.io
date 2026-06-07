---
layout: text-page
title: Orbital Simulation in Fortran
---
# simulating gravitational orbits with fortran

The orbital simulation project began as the final assignment for a
Computational Astrophysics module offered at the University of St Andrews.
The aim was to create a program using Fortran that would solve for the
motion of N bodies under their mutual gravitational interaction. Over a series of
time steps the positions and velocities of each body were stored in an array,
which was then written to an external file so that the
orbital paths could be visualised using the Matplotlib Python library.

Physical accuracy of the simulation was tested using three parameters: conservation of
momentum, conservation of energy, and conservation of position after one closed orbit.

![Six-body simulation in a spherically symmetric mean galactic potential](/static/images/OrbitSimImages/GalaxyMany.png){:.content-image}
*Six-body simulation in a spherically symmetric mean galactic potential*

![The same simulation in an asymmetric mean galactic potential](/static/images/OrbitSimImages/GalaxyManySquished.png){:.content-image}
*The same simulation in an asymmetric mean galactic potential*


## why fortran?

Fortran has maintained a steady usage in the computational sciences for
its speed and optimisation. It is a language designed for high-speed
numerical operations, making it ideal for a basic orbital simulator
where the main computational component was the solving of a second order
differential equation. Learning
to work with a compiled language took a degree of patience for me, having
only ever used Python before, but I know that had I attempted this project
in Python I would have become swamped in unnecessary for-loops and list
appendages - something Fortran simply does not allow you to do.


## visualisation with matplotlib

Plotting static orbit paths from the resulting data files was as easy as loading
them into a Python file and generating a matplotlib graph, which is exactly what I
did for the two images above.

The advantage to animated visualisation of the data was that erratic behaviour was easier
to diagnose. However, when it came to animating the orbits a tradeoff had to be made.
The variable timestep that I had implemented meant that the orbits seemed to slow down whenever
two or more massive bodies approached each other. This was due to the animation process
assuming that each position vector was recorded at an equal timestep.