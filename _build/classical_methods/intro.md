---
redirect_from:
  - "/classical-methods/intro"
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
These can be molecular dynamics (which we will cover in this module), Monte Carlo, Langevin dynamics, etc.

In order to simulate a **real** chemical system, it is necessary to model the electrons and their interactions.
This is achieved by using quantum mechanical calculations, where the energy of a chemical system is calculated by finding an approximate solution to the Schrödinger equation.
However, these calculations are **very** computationally expensive, and are therefore realistically limited to hundreds of atoms.

The Born-Oppenheimer approximation assumes that the potential energy of a given system depends only on the positions of the nuclei.
With this assumption envoked, it is possible to find the potential energy using two approaches.
The first is some ground-state quantum mechanical method (e.g. density functional theory), however as mentioned above these are limited in system size.
The alternative involves modelling the electron distributions with some mathematical function to determine the potential energy.
These **potential models** are usually faster to calculate than the quantum mechanical method and therefore may be used on larger systems.
However, this **simplification** does have a drawback in that the correct potential models must be determined for each system to accurately determine the energy. 
