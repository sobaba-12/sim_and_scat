---
redirect_from:
  - "/calculating-scattering/debye-equation"
interact_link: content/calculating_scattering/debye_equation.ipynb
title: 'The Debye equation'
prev_page:
  url: /calculating_scattering/rdfs
  title: 'Radial Distribution Functions'
next_page:
  url: /calculating_scattering/temp
  title: 'Temperature'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## The Debye equation

The Debye equation is an **analytical** formulation to determine the scattering that arises from some system. 
In many ways, the Debye equation can be thought of as a weighted, analytical Fourier transform of the radial distribution function. 
It is weighted by the scattering length of the particular particles being considered, $b_i$ and $b_j$.
This equation considers the distances between particles, $r_{ij}$, to determine the scattered intensity at a given $q$-vector, $I(q)$, 

$$ I(q) = \sum_i\sum_jb_ib_j\frac{\sin{(qr_{ij})}}{qr_{ij}}. $$

While this equation is analytically-precise, there are some **problems** with this method. 
In particular, that it requires a **pair-wise summation**, which is very slow for large systems such as those obtained in molecular dynamics.

The Python code below is a simple implimentation of the Debye function, where the scattering length is taken as 1.909 fm (the $b$ for argon) for all particles.
Try different values for the scattering length, and observe how the resulting profile changes. 



{:.input_area}
```python
import numpy as np

def debye(qvalues, xposition, yposition, box_length, b):
    """
    Calculates the scattering profile from the 
    simulation 
    positions.
    
    Parameters
    ----------
    qvalues: float, array-like
        The q-vectors over which the scattering 
        should be calculated
    xposition: float, array-like
        The positions of the particles in the x-axis
    yposition: float, array-like
        The positions of the particles in the y-axis
    box_length: float
        The length of the simulation square
        
    Returns
    -------
    intensity: float, array-like
        The calculated scattered intensity
    """
    intensity = np.zeros_like(qvalues)
    for e, q in enumerate(qvalues):
        for m in range(0, xposition.size-1):
            for n in range(m+1, xposition.size):
                xdist = xposition[n] - xposition[m]
                xdist = xdist % box_length
                ydist = yposition[n] - yposition[m]
                ydist = ydist % box_length
                r_mn = np.sqrt(np.square(xdist) + np.square(ydist))
                intensity[e] += b * b * np.sin(
                    r_mn * q) / (r_mn * q)
        if intensity[e] < 0:
            intensity[e] = 0
    return intensity
            
from pylj import md, sample

def md_simulation(number_of_particles, temperature, 
                  box_length, number_of_steps, 
                  sample_frequency):
    """
    Runs a molecular dynamics simulation in using the pylj 
    molecular dynamics engine.
    
    Parameters
    ----------
    number_of_particles: int
        The number of particles in the simulation
    temperature: float
        The temperature for the initialisation and 
        thermostating
    box_length: float
        The length of the simulation square
    number_of_steps: int
        The number of molecular dynamics steps to run
    sample_frequency: 
        How regularly the visualisation should be updated
        
    Returns
    -------
    pylj.util.System
        The complete system information from pylj
    """
    %matplotlib notebook
    system = md.initialise(number_of_particles, temperature, 
                           box_length, 'square')
    sample_system = sample.CellPlus(system, 
                                    'q/m$^{-1}$', 'I(q) / m$^2$')
    system.time = 0
    for i in range(0, number_of_steps):
        system.integrate(md.velocity_verlet)
        system.md_sample()
        system.heat_bath(temperature)
        system.time += system.timestep_length
        system.step += 1
        if system.step % sample_frequency == 0:
            min_q = 2. * np.pi / box_length
            qs = np.linspace(min_q, 10e10, 120)[20:]
            inten = debye(qs, system.particles['xposition'], 
                          system.particles['yposition'], 
                          box_length, 1.909e-15)
            sample_system.update(system, qs, inten)
    return system

system = md_simulation(10, 3, 15, 5000, 10)
```

