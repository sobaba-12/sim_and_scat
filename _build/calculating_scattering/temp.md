---
redirect_from:
  - "/calculating-scattering/temp"
interact_link: content/calculating_scattering/temp.ipynb
title: 'Temperature'
prev_page:
  url: /calculating_scattering/debye_equation
  title: 'The Debye equation'
next_page:
  url: /calculating_scattering/scaling
  title: 'Scaling'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

## Temperature effects

Try varying the temperature of the simulation, through values of 3, 30, and 300 K, and watch the scattering profile for the presence of Bragg peaks in the data when the system is cold enough to freeze.
Compare this to the radial distribution functions discussed previously.



{:.input_area}
```python
import numpy as np

def debye(qvalues, xposition, yposition, box_length):
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
                intensity[e] += 1 * 1 * np.sin(
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
                                    'q/m$^{-1}$', 'I(q)')
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
                          box_length)
            sample_system.update(system, qs, inten)
    return system

system = md_simulation(10, 3, 15, 5000, 10)
```

