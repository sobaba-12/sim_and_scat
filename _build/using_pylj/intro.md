---
redirect_from:
  - "/using-pylj/intro"
interact_link: content/using_pylj/intro.ipynb
title: 'Using pylj'
prev_page:
  url: /important_considerations/pbc
  title: 'Periodic boundary conditions'
next_page:
  url: /calculating_scattering/intro
  title: 'Calculating scattering'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---

# Using pylj

pylj is an open-source tool for **enabling interaction between students** (the user of this tutorials) and molecular dynamics simulations [[1,2](#references)]. 
This software enables the simulation of argon atoms in a two-dimensional box. 
The Python code below runs a pylj molecular dynamics simulation. 



{:.input_area}
```python
from pylj import md, sample

def md_simulation(number_of_particles, temperature, box_length, number_of_steps, sample_frequency):
    """
    Runs a molecular dynamics simulation in suing the pylj molecular dynamics engine.
    
    Parameters
    ----------
    number_of_particles: int
        The number of particles in the simulation
    temperature: float
        The temperature for the initialisation and thermostating
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
    # Creates the visualisation environment
    %matplotlib notebook
    # Initialise the system
    system = md.initialise(number_of_particles, temperature, box_length, 'square')
    # This sets the sampling class
    sample_system = sample.JustCell(system)
    # Start at time 0
    system.time = 0
    # Begin the molecular dynamics loop
    for i in range(0, number_of_steps):
        # Run the equations of motion integrator algorithm, this 
        # includes the force calculation
        system.integrate(md.velocity_verlet)
        # Sample the thermodynamic and structural parameters of the system
        system.md_sample()
        # Allow the system to interact with a heat bath
        system.heat_bath(temperature)
        # Iterate the time
        system.time += system.timestep_length
        system.step += 1
        # At a given frequency sample the positions and plot the RDF
        if system.step % sample_frequency == 0:
            sample_system.update(system)
    return system

system = md_simulation(20, 300, 20, 5000, 10)
```


The functionality of pylj that we will be using is the ability to **add custom plots** to the interface, as well as the storing of information about the particle positions.
This is can be observed with the Python code below for the instanteous temperature of the simulation being performed.



{:.input_area}
```python
import numpy as np
from pylj import md, sample

def md_simulation(number_of_particles, temperature, box_length, number_of_steps, sample_frequency):
    """
    Runs a molecular dynamics simulation in suing the pylj molecular dynamics engine.
    
    Parameters
    ----------
    number_of_particles: int
        The number of particles in the simulation
    temperature: float
        The temperature for the initialisation and thermostating
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
    system = md.initialise(number_of_particles, temperature, box_length, 'square')
    sample_system = sample.CellPlus(system, 'Time/s', 'Temperature/K')
    system.time = 0
    for i in range(0, number_of_steps):
        system.integrate(md.velocity_verlet)
        system.md_sample()
        system.heat_bath(temperature)
        system.time += system.timestep_length
        system.step += 1
        if system.step % sample_frequency == 0:
            sample_system.update(system, np.linspace(0, system.time, system.step), system.temperature_sample)
    return system

system = md_simulation(20, 300, 20, 5000, 10)
```


It can be seen that there are two differences to add the custom plot. 
Firstly, there is the use of the `sample.CellPlus` class, which requires the definition of the labels for the x- and y-axes of the plot. 
Secondly, there is the inclusion of the <i>x</i>- and <i>y</i>-data to be plotted in the `sample_system.update` line. 
In the above example these are `np.linspace(0, system.time, system.step)` (which is an array from 0 to the particular simulation timestep at that moment) and `system.temperature_sample` which is an array of the instaneous temperature at each timestep in the simulation. 

In the next episode we will take advantage of these features to better understand how to determine the scattering profile from the simulation cell. 

# References

1. McCluskey, A. R.; Morgan, B. J.; Edler, K. J.; Parker, S. C. *J. Open Source Educ.* 2018, **1** (2), 19. [10.21105/jose.00019](https://doi.org/10.21105/jose.00019).
2. McCluskey, A. R.; Symington, A. R. arm61/pylj: pylj-1.2.1 [10.5281/zenodo.2423866](http://doi.org/10.5281/zenodo.2423866).
