---
redirect_from:
  - "/parameterisation/off-the-shelf"
title: 'Off-the-shelf potentials'
prev_page:
  url: /parameterisation/intro
  title: 'Parameterisation'
next_page:
  url: /parameterisation/mixing_rules
  title: 'Mixing rules'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
## Off-the-shelf potentials

In an effort to counter the problem of having to develop a new forcefield *every* time someone wanted to perform a molecular dynamics simulation, a variety of off-the-shelf potentials have been developed.
These are *general* forcefields that as designed to be applied to any system.

Although a potential model has been developed with the aim of *generality*, they should still be used with **caution**.
The chemistry of your system may not directly match the system used in the potential generation, which can lead to systematic errors in your the simulations.

Some examples of off-the-shelf potentials include:
- AMBER: popular for DNA and proteins
- CFF: designed for a broad variety of organic compounds
- CHARMM: widely used for small molecules
- GROMOS: common for biomolecular systems
- OPLS-AA: optimised for liquid simulations

These can be applied to many systems, however, as mentioned above, they should be used with caution.
One way to assess the suitability of an off-the-shelf potential is to use it to reproduce some simple, but known, property of the material, e.g. its density. 
