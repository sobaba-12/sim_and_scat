## Ensembles

The molecular dynamics algorithm outlined in the previous lesson makes use of the NVE ensemble (also known as the microcanonical ensemble), where the number of particles (N), volume of the system (V), and energy of the system (E) are all **kept constant**.
This is not the only, or the most accurate, ensemble that exists, there is also other such as:
- NVT (canonical): number of particles (N), volume of system (V), temperature of the simulation (T)
- NPT (isothermal-isobaric): number of particles (N), pressure of system (P), temperature of the simulation (T)

For both the canonical and isothermal-isobaric ensembles, it is necessary to determine a method to **modulate the temperature** of the system.
The temperature can be modulated using a variety of methods known as thermostating.
The simplest, although one of the least accruate, is velocity rescaling.
This is where the velocities of the individual particles are changed such that the kinetic energy of the total system more accurately matches that necessary for the desired temperature.
For this the instaneous temperature of the system, $T_{\text{inst}}$, is defined as,

$$ T_{\text{inst}} = \frac{\sum^N_{i=0}{m_i v_i^2}}{2Nk_B}, $$

where, $N$ is the number of particles, $m_i$ is the mass of particle $i$, $v_i$ is the velocity of particle $i$, and $k_B$ is the Boltzmann constant.
This means that the velocities of the particles may be rescaled by the following relation,

$$ \mathbf{v}_i = \mathbf{v}_i \sqrt{\dfrac{T_{\text{target}}}{\bar{T}}}, $$

where $\mathbf{v}_i$ is the velocity of particle $i$, $T_{\text{target}}$ is the target temperature for the themostat, and $\bar{T}$ is the average simulation temperature.
pylj [[1,2](#references)], to software that you shall use in the next lesson uses this method for producing an NVT simulation, using the `heat_bath` function.
Various **other methods** for thermostating exist, such as the Anderson, Nosé-Hoover, or the Berendsen [[3-6](#references)].

In order to achieve the NPT ensemble, it is necessary to use a **barostat** in addition to a thermostat.
These allow the volume of the system to vary such that the pressure is constant throughout the simulation.
We will not discuss barostats any further, but there is plenty of information in more detailed texts.

## References

1. McCluskey, A. R.; Morgan, B. J.; Edler, K. J.; Parker, S. C. *J. Open Source Educ.* 2018, **1** (2), 19. [10.21105/jose.00019](https://doi.org/10.21105/jose.00019).
2. McCluskey, A. R.; Symington, A. R. [10.5281/zenodo.2423866](http://doi.org/10.5281/zenodo.2423866).
3. Andersen, H. C. *J. Chem. Phys.* 1980, **72** (4), 2384–2393. [10.1063/1.439486](https://doi.org/10.1063/1.439486).
4. Nosé, S. *J. Chem. Phys.* 1984, **81** (1), 511–519. [10.1063/1.447334](https://doi.org/10.1063/1.44733410.1063/1.447334.
5. Berendsen, H. J. C.; Postma, J. P. M.; van Gunsteren, W. F.; DiNola, A.; Haak, J. R. *J. Chem. Phys.* 1984, **81** (8), 3684–3690. [10.1063/1.448118](https://doi.org/10.1063/1.448118).
6. Hoover, W. G. *Phys. Rev. A* 1985, **31** (3), 1695–1697. [10.1103/PhysRevA.31.1695](https://doi.org/10.1103/PhysRevA.31.1695).
