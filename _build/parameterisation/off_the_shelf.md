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
# Off-the-shelf potentials

In an effort to counter the problem of developing a new forcefield *every* time a different MD simulation is to be performed, a variety of off-the-shelf potentials have been developed.
These aspire to be *general* forcefields to be applied to any system.

Although these potential models are developed with the aim of *generality*, they should still be used with **caution**.
The chemistry of your system may not directly match the system used in the potential generation, which can lead to systematic errors in your the simulations.

Some examples of off-the-shelf potentials include:
- AMBER: popular for DNA and proteins [[1](#References)]
- CFF: designed for a broad variety of organic compounds [[2](#References)]
- CHARMM: widely used for small molecules [[3](#References)]
- GROMOS: common for biomolecular systems [[4](#References)]
- OPLS-AA: optimised for liquid simulations [[5](#References)]

These can be applied to many systems, however, as mentioned above, they should be used with care.
One way to assess the suitability of an off-the-shelf potential is to to reproduce a simple, but well-defined, property of the material, e.g. density. 

## References

1. Cornell, W. D.; Cieplak, P.; Bayly, C. I.; Gould, I. R.; Merz, K. M.; Ferguson, D. M.; Spellmeyer, D. C.; Fox, T.; Caldwell, J. W.; Kollman, P. A. *J. Am. Chem. Soc.* 1995, **117** (19), 5179–5197. [10.1021/ja00124a002](https://doi.org/10.1021/ja00124a002).
2. Lifson, S.; Warshel, *J. Chem. Phys.* 1968, **49** (11), 5116–5129. [10.1063/1.1670007](https://doi.org/10.1063/1.1670007).
3. MacKerell, A. D.; Banavali, N.; Foloppe, N. *Biopolymers* 2000, **56** (4), 257–265. [10.1002/1097-0282(2000)56:4<257::AID-BIP10029>3.0.CO;2-W](https://doi.org/10.1002/1097-0282(2000)56:4<257::AID-BIP10029>3.0.CO;2-W).
4. Reif, M. M.; Winger, M.; Oostenbrink, C. *J. Chem. Theory Comput.* 2013, **9** (2), 1247–1264. [10.1021/ct300874c](https://doi.org/10.1021/ct300874c).
5. Jorgensen, W. L.; Tirado-Rives, J. *J. Am. Chem. Soc.* 1988, **110** (6), 1657–1666. [10.1021/ja00214a001](https://doi.org/10.1021/ja00214a001).