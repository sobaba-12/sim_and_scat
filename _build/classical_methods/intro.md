---
redirect_from:
  - "/classical-methods/intro"
interact_link: content/classical_methods/intro.ipynb
title: 'Classical methods'
prev_page:
  url: /intro
  title: 'Home'
next_page:
  url: /classical_methods/potential_models
  title: 'Potential models'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Classical methods

**Classical methods** is a phrase used to describe techniques that make use of a potential model (sometimes called a force-field) to simulated chemical systems.
Examples are molecular dynamics (which we will cover in this resource), Monte Carlo, Langevin dynamics, etc.

The Born-Oppenheimer approximation allows the motions of the nuclei and the electrons to be separated, due to the large difference in their size.
This gives theoretical chemistry two options for how to model a chemical system, and determine the potential energy and therefore the mostly likely configuration: 
- treat the nuclei as stationary and model the motions and interactions of the electrons using the Schrödinger equation
- to integrate the motions of the electrons into the nuclei and model these particles as point charges

The former is the basis for quantum mechanical calculations, such as density functional theory (DFT) methods. 
In these methods, the aim is to find an iterative solution to the Schrödinger equation. 
However, these methods are **very** computationally expensive, and are therefore realistically limited to hundreds or thousands of atoms [[1](#References)]. 
We will not discuss quantum mechanical methods more than this, for more information there are many great textbooks on the subject [[2,3](#References)]. 

The latter methods are what are known as **classical methods**.
Classical methods involved the use of a potential model (sometimes called a force-field) to simulate chemical systems. 
Examples of simulations techniques that may leverage classical methods include molecular dynamics (which we will cover in this resource), Monte Carlo, Langevin dynamics, etc.
A potential model uses mathematical functions to determine the potential energy of a given configuration of atoms. 
The use of mathematical functions to model the interactions of the particles is less computationally expensive than quantum mechanical methods meaning that it is possible to simulated larger systems. 

An example of a classical method can be seen below where the particles have only a var der Waals interaction, which is a good model for argon gas.
The number in the function is the temperature of the simulation in Kelvin. 
Click the "Interact" button above to launch an interactive MyBinder page, you can then run the simulation at a series of different temperatures and see how the particles move. 



{:.input_area}
```python
import vdw
%matplotlib notebook
vdw.simulation(300)
```


## References

1. Erba, A.; Baima, J.; Bush, I.; Orlando, R.; Dovesi, R. *J. Chem. Theory Comput.* 2017, **13** (10), 5019–5027. [10.1021/acs.jctc.7b00687](https://doi.org/10.1021/acs.jctc.7b00687).
2. Harvey, J. *Computational Chemistry*; Oxford University Press: Oxford, 2018.
3. Atkins, P. W.; Friedmann, R. S. *Molecular Quantum Mechanics*, 5th ed.; Oxford University Press: Oxford, 2010.
