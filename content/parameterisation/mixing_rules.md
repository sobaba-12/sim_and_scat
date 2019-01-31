## Mixing rules

Generally these off-the-shelf potentials only give the van der Waals potential for a self interaction.
This is the interaction of a particular atom with another atom of the same type, e.g. an argon-argon interaction.
This allows the off-the-shelf potential can be more concise.
However, it is necessary to determine how the different atom types **interact with each other**.
This is achieved through the application of mixing rules, which provide a way to calculate the interaction potentials of different atoms interacting with each other.

One of the most common types of mixing rules are the **Lorentz-Berthelot** rules [[1, 2](#references)].
These are as follows,

$$ \sigma_{ij} = \dfrac{\sigma_{ii} + \sigma_{jj}}{2} \;\;\;\text{and}\;\;\; \varepsilon_{ij} = \sqrt{\varepsilon_{ii}\varepsilon_{jj}}, $$

where $\sigma$ and $\varepsilon$ are familiar from the Lennard-Jones potential, while the subscript differentiate self- and mixed-interactions.

As with the determination of the potentials itself, the ways in which these potentials can be mixed can vary considerably and there is no single rule for all systems.
To give further insight into the variation possible, the Wikipedia entry on [combining rules](https://en.wikipedia.org/wiki/Combining_rules) provides an introduction into some of the rule sets commonly employed.

## References

1. Lorentz, H. A. *Ann. Phys.* 1881, **248** (1), 1227–136. [10.1002/andp.18812480110](https://doi.org/10.1002/andp.18812480110).
2. Berthelot, D. *Comptes. Rendus. Acad. Sci.* 1898, **126**, 1703–1855.
