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

**Classical molecular dynamics** (MD) is a common computational chemistry technique for studying complex systems, such as proteins, polymers, and energy materials [[1-4](#references)]. Alongside the interest in these and other applications, molecular dynamics is also a used to aid the analysis of data obtained from elastic scattering instruments.

This tutorial has been written to **introduce users of elastic-scattering techniques**, such as small angle scattering or diffraction, to classical molecular dynamics (MD) simulation. We aim to provide an accessible route for experimentalists to **better understand some of the complexities and subtleties of MD simulation**, thereby aiding these researchers in extracting additional information from theiry data via simulation.

This tutorial begins with an introduction to classical simulation methods, including a discussion of the development and parameterisation of classical interatomic potential models. We then provide an outline of traditional molecular dynamics simulation methods and discuss a number of important considerations users of MD simulation should be aware of. We close this tutorial with an illustrative practical example, using the open-source Lennard-Jones simulation package [`pylj`](http://pythoninchemistry.org/pylj) [[5,6](#references)], and discuss how a radially averaged scattering profile may be obtained **directly from simulation** via the Debye equation [[7](#references)].

We wish to emphasise that this tutorial is in **no way** a complete course on molecular dynamics, and would direct the interested reader to one of the many detailed textbooks on this subject [[8-12](#references)]. Rather, it is our hope that this tutorial provides a simple, practical, **general introduction to new, or future, users of MD methods within the scattering community**.

## Prerequisites

To get the most from this tutorial you will need:

- Some basic understanding of the Python programming language (a great source for learning some Python is [pythoninchemistry.org](http://pythoninchemistry.org))
- Some knowledge of undergraduate chemistry or physics is be required to fully appreciate the nature of classical potential models.
- A commensurate understanding of mathematics.

## Using this resource

This resource is designed to be interactive, which is achieved using [Thebelab](https://github.com/minrk/thebelab) and [BinderHub](https://binderhub.readthedocs.io/en/latest/) integration.
Each page that contains interactive content will have the following two buttons at the top,

![](./images/thebebinder.png)

Selecting the "Interact" button will open a Jupyter Notebook version of the page running on the [MyBinder](https://mybinder.org) resource in a new tab.
The "Thebelab" button will make the code blocks in the webpage interactive, they can be run, edited, and re-run.
The Thebelab integration is still in beta and therefore will not work perfectly every time (it is known not to work for the pylj examples towards the end).
When the Thebelab integration fails, please use the Interact button.

If you would prefer to run the resource locally, details of how this can be achieved can be found [here](https://github.com/pythoninchemistry/sim_and_scat/blob/master/content/local.md).

## Code (in)efficiency

Please be aware that the Python code written in this tutorial has been written to prioritise understanding, above computational efficiency. 
Individual examples may therefore not be be the most efficient implementation of particular algorithms. 
However, we have endeavoured to provide code examples that are *authentic*, and accurately represent the relevant aspects of *real* molecular dynamics methods.

## Sharing this resource

This is an open educational resource, shared under a [CC BY-SA 4.0 license](./LICENSE.md).
This means that anyone is free to copy and redistribute the resource in any medium or format and welcome to remix, transform, and build upon the material for any purpose, even commercially.
Basically you can do whatever you want with it, although we would appreciate if you would reference the original resource if you use it.
Please use the reference below, or download it has a [BibTeX file](./sim_and_scat.bib).
> McCluskey, A. R. [10.5281/zenodo.2543277](http://doi.org/10.5281/zenodo.2543277)

## Authors

This open educational resource was originally developed by [Andrew R. McCluskey](https://orcid.org/0000-0003-3381-5911) during his PhD at the University of Bath and Diamond Light Source.
The following people contributed substantially to the resource:
- [James Grant](https://orcid.org/0000-0003-1362-2055)
- [Adam R. Symington](https://orcid.org/0000-0001-6059-497X)
- [Tim Snow](https://orcid.org/0000-0001-7146-6885)
- James Doutch
- [Benjamin J. Morgan](https://orcid.org/0000-0002-3056-8233)
- [Stephen C. Parker](https://orcid.org/0000-0003-3804-0975)
- [Karen J. Edler](https://orcid.org/0000-0001-5822-0127)

## Acknowledgements

A. R. M. is grateful to the University of Bath and Diamond Light Source for co-funding a studentship (Studentship No. STU0149).
B. J. M. acknowledges support from the Royal Society (Grant No. UF130329).

## References

1. Karplus, M.; McCammon, J. A. *Nat. Struct. Biol.* 2002, **9** (9), 7. [10.1038/nsb0902-646](https://doi.org/10.1038/nsb0902-646).
2. Binder, K. *Monte Carlo and Molecular Dynamics Simulations in Polymer Science*; Oxford University Press: Oxford, 1995.
3. Kim, S.-P.; van Duin, A. C. T.; Shenoy, V. B. *J. Power Sources* 2011, **196** (20), 8590–8597. [10.1016/j.jpowsour.2011.05.061](https://doi.org/10.1016/j.jpowsour.2011.05.061).
4. Burbano, M.; Carlier, D.; Boucher, F.; Morgan, B. J.; Salanne, M. *Phys. Rev. Lett.* 2016, **116** (13). [10.1103/PhysRevLett.116.135901](https://doi.org/10.1103/PhysRevLett.116.135901).
5. McCluskey, A. R.; Morgan, B. J.; Edler, K. J.; Parker, S. C. *J. Open Source Educ.* 2018, **1** (2), 19. [10.21105/jose.00019](https://doi.org/10.21105/jose.00019).
6. McCluskey, A. R.; Symington, A. R. [10.5281/zenodo.2423866](http://doi.org/10.5281/zenodo.2423866).
7. Debye, P. *Ann. Phys.* 1915, **351** (6), 809–823. [10.1002/andp.19153510606](https://doi.org/10.1002/andp.19153510606).
8. Harvey, J. *Computational Chemistry*; Oxford University Press: Oxford, 2018.
9. Grant, G. H.; Richards, W. G. *Computational Chemistry*; Oxford University Press: Oxford, 1995.
10. Leach, A. R. *Molecular Modelling: Principles and Applications*; Addison Wesley London Ltd: Harlow, 1996.
11. Frenkel, D.; Smit, B. *Understanding Molecular Simulation: From Algorithms to Applications*; Academic Press: San Diego, 1996.
12. Allen, M. P.; Tildesley, D. J. *Computer Simulation of Liquids*, 2nd ed.; Oxford University Press: Oxford, 2017.
