---
redirect_from:
  - "/"
title: 'Home'
prev_page:
  url: 
  title: ''
next_page:
  url: /classical_methods/intro
  title: 'Classical methods'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# The interaction between simulation and scattering

**Classical molecular dynamics** (MD) is a common computational chemistry technique for studying complex systems, such as proteins, polymers, and battery materials. Alongside the interest in these and other applications, molecular dynamics is also a used to help analyse data obtained from elastic scattering instruments.

This tutorial has been written to **introduce users of elastic-scattering techniques**, such as small angle scattering or diffraction, to classical molecular dynamics (MD) simulation. We hope that this tutorial can provide an accessible route for experimental researchers to **better understand some of the complexities and subtleties of MD simulation**, thereby helping these researchers to get more relevant information from their simulations.

This tutorial begins with an introduction to classical simulation methods, including a discussion of the development and parameterisation of classical interatomic potential models. We then provide an outline of traditional molecular dynamics simulation methods and discuss a number of important considerations users of MD simulation should be aware of. We close this tutorial with an illustrative practical example, using the open-source Lennard-Jones simulation package [`pylj`](http://pythoninchemistry.org/pylj), and discuss how a radially averaged scattering profile may be obtained **directly from simulation** via the Debye equation.

We wish to emphasise that this tutorial is in **no way** a complete course on molecular dynamics, and would direct the interested reader to one of the many detailed textbooks on this subject. Rather, it is our hope that this tutorial provides a simple, practical, **general introduction to new, or future, users of MD methods within the scattering community**.

## Prerequisites

To get the most from this tutorial you will need:

- Some basic understanding of the Python programming language (a great source for learning some Python is [pythoninchemistry.org](http://pythoninchemistry.org))
- Some knowledge of undergraduate chemistry or physics may be required to fully appreciate the nature of classical potential models.
- A decent understanding of advanced high school level mathematics.

## Code (in)efficiency

Please be aware that the Python code written in this tutorial has been written to prioritise understanding, above computational efficiency. Individual examples may therefore not be be the most efficient implementation of particular algorithms. That said, we have endeavoured to provide code examples that are “authentic”, and accurately represent the relevant aspects of “real” molecular dynamics methods.

## Authors

This open educational resource was originally developed by [Andrew R. McCluskey](https://orcid.org/0000-0003-3381-5911)<sup>a,b</sup>, with significant input from [Adam R. Symington](https://orcid.org/0000-0001-6059-497X)<sup>a</sup>, [Tim Snow](https://orcid.org/0000-0001-7146-6885)<sup>b</sup>, [James Grant](https://orcid.org/0000-0003-1362-2055)<sup>c</sup>, [Benjamin J. Morgan](https://orcid.org/0000-0002-3056-8233)<sup>a</sup>, [Stephen C. Parker](https://orcid.org/0000-0003-3804-0975)<sup>a</sup>, and [Karen J. Edler](https://orcid.org/0000-0001-5822-0127)<sup>a</sup>.

a. Department of Chemistry, University of Bath, Claverton Down, Bath BA2 7AY, UK
<br>b. Diamond Light Source, Diamond House, Rutherford Appleton Laboratory, Harwell Oxford, OX11 0DE, UK
<br>c. Computing Services, University of Bath, Claverton Down, Bath, BA2 7AY, UK


## References
