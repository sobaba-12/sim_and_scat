---
redirect_from:
  - "/classical-methods/bonds"
interact_link: content/classical_methods/bonds.ipynb
title: 'Bonds'
prev_page:
  url: /classical_methods/coulomb
  title: 'Charged interactions'
next_page:
  url: /classical_methods/potential_models
  title: 'Potential models'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Bonds

Tha ability to simulate atoms interacting through the van der Waals and charged interactions is useful for the study of non-covalent materials. 
However, to truely probe the chemistry of a system we must also be able to model the bonded interactions. 

The potential energy of the bonded interactions of a system is usually made up of bonds, angles, dihedrals, and other higher order processes,

$$ E_{\text{bonded}} = E_{\text{bond}}(b) + E_{\text{angle}}(\theta) + E_{\text{dihedral}}(\phi) + \ldots . $$

We will focus just on the first two, more information about the higher order processes can be found in relevent textbooks (see [Home](http://pythoninchemistry.org/sim_and_scat/intro#references)). 
The bond lengths are typically modelled with a harmonic potential energy function, 

$$ E_{\text{bond}}(\mathbf{r}) = \frac{K_b}{2}(b - b_0)^2, $$

where, $b_0$ is the equilibrium bond length and $K_b$ is the force constant for the bond. 
These must be determined (see [Parameterisation](http://pythoninchemistry.org/sim_and_scat/parameterisation/intro)), and $b$ is the measured bond length. 
An example of this function can be seen below, using the parameters of a carbon-carbon bond.



{:.input_area}
```python
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

def bonded(kb, b0, b):
    """
    Calculation of the potential energy of a bond.
    
    Parameters
    ----------
    kb: float
        Bond force constant (units: eV/Å^2)
    b0: float 
        Equilibrium bond length (units: Å)
    b: float
        Bond length (units: Å)
    
    Returns
    float
        Energy of the bonded interaction
    """
    return kb / 2 * (r - b0) ** 2

r = np.linspace(1, 2, 100)
plt.plot(r, bonded(274965.16, 1.522, r))
plt.xlabel(r'$r$/Å')
plt.ylabel(r'$E$/eV')
plt.show()
```



{:.output .output_png}
![png](../images/classical_methods/bonds_1_0.png)



Using this harmonic function the bond length is modelled such that minimum if at the equilibrium bond length and both increasing and decreasing the length will increase the energy equally.

The potential energy of an angle between two atoms that are separated by a third is modeled with a similar harmonic function, 

$$ E_{\text{angle}}(\theta) = \frac{K_\theta}{2}(\theta - \theta_0)^2, $$

where, $\theta$ is the measured angle, $K_\theta$ is the force constant for the angle, and $\theta_0$ is the equilibrium angle size. 
This has the same shape as the bond potential energy curve shown above.

Activate the interactive MyBinder environment (by clicking the "Interact" button at the top). 
This will allow the code cell below to be run. 
This simulation shows a single diatomic molecule interacting through a single bond modelled with a harmonic potential model. 
Again, you can vary the temperature of the simulation and observe how the bond vibration changes. 



{:.input_area}
```python
import bond
%matplotlib notebook
bond.simulation(100)
```


For the sake of simplicity, the remainder of this resource will only focus on non-bonded interactions. 
However, it is important to be aware that all aspects discussed are **equally applicable** to bonded interactions.
