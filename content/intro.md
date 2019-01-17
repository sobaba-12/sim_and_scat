# The interaction between simulation and scattering

**Classical molecular dynamics** (MD) is a common computational chemistry technique for studying complex systems, such as proteins, polymers, and battery materials [1-4]. Alongside the interest in these and other applications, molecular dynamics is also a used to help analyse data obtained from elastic scattering instruments.

This tutorial has been written to **introduce users of elastic-scattering techniques**, such as small angle scattering or diffraction, to classical molecular dynamics (MD) simulation. We hope that this tutorial can provide an accessible route for experimental researchers to **better understand some of the complexities and subtleties of MD simulation**, thereby helping these researchers to get more relevant information from their simulations.

This tutorial begins with an introduction to classical simulation methods, including a discussion of the development and parameterisation of classical interatomic potential models. We then provide an outline of traditional molecular dynamics simulation methods and discuss a number of important considerations users of MD simulation should be aware of. We close this tutorial with an illustrative practical example, using the open-source Lennard-Jones simulation package [`pylj`](http://pythoninchemistry.org/pylj) [5,6], and discuss how a radially averaged scattering profile may be obtained **directly from simulation** via the Debye equation [6].

We wish to emphasise that this tutorial is in **no way** a complete course on molecular dynamics, and would direct the interested reader to one of the many detailed textbooks on this subject [8-12]. Rather, it is our hope that this tutorial provides a simple, practical, **general introduction to new, or future, users of MD methods within the scattering community**.

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

1. Karplus, M.; McCammon, J. A. *Nat. Struct. Biol.* 2002, **9** (9), 7. [10.1038/nsb0902-646](https://doi.org/10.1038/nsb0902-646).
2. Binder, K. *Monte Carlo and Molecular Dynamics Simulations in Polymer Science*; Oxford University Press: Oxford, 1995.
3. Kim, S.-P.; van Duin, A. C. T.; Shenoy, V. B. *J. Power Sources* 2011, **196** (20), 8590–8597. [10.1016/j.jpowsour.2011.05.061](https://doi.org/10.1016/j.jpowsour.2011.05.061).
4. Burbano, M.; Carlier, D.; Boucher, F.; Morgan, B. J.; Salanne, M. *Phys. Rev. Lett.* 2016, **116** (13). [10.1103/PhysRevLett.116.135901](https://doi.org/10.1103/PhysRevLett.116.135901).
5. McCluskey, A. R.; Morgan, B. J.; Edler, K. J.; Parker, S. C. *J. Open Source Educ.* 2018, **1** (2), 19. [10.21105/jose.00019](https://doi.org/10.21105/jose.00019).
6. McCluskey, A. R.; Symington, A. R. arm61/pylj: pylj-1.2.1 [10.5281/zenodo.2423866](http://doi.org/10.5281/zenodo.2423866).
7. Debye, P. *Ann. Phys.* 1915, **351** (6), 809–823. [10.1002/andp.19153510606](https://doi.org/10.1002/andp.19153510606).
8. Harvey, J. *Computational Chemistry*; Oxford University Press: Oxford, 2018.
9. Grant, G. H.; Richards, W. G. *Computational Chemistry*; Oxford University Press: Oxford, 1995.
10. Leach, A. R. *Molecular Modelling: Principles and Applications*; Addison Wesley London Ltd: Harlow, 1996.
11. Frenkel, D.; Smit, B. *Understanding Molecular Simulation: From Algorithms to Applications*; Academic Press: San Diego, 1996.
12. Allen, M. P.; Tildesley, D. J. *Computer Simulation of Liquids*, 2nd ed.; Oxford University Press: Oxford, 2017.
