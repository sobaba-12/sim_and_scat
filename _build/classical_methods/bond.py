import numpy as np
from pylj import md, sample
from numba import jit

@jit
def bond(dr, constants, force=False):
    r"""Calculate the energy or force for a pair of particles using a harmonic
    potential.

    .. math::
        E = K/2(dr - b)^2

    .. math::
        f = K(dr-b)

    Parameters
    ----------
    dr: float, array_like
        The distances between the all pairs of particles.
    constants: float, array_like
        An array of length two consisting of the K and b parameters for the
        harmonic function.
    force: bool (optional)
        If true, the negative first derivative will be found.

    Returns
    -------
    float:
        The potential energy or force between the particles.
    """
    if force:
        return constants[0] * (np.abs(dr) - constants[1])
    else:
        return constants[0] / 2. * np.power((dr - constants[1]), 2)

def simulation(temperature, a, b):
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
    # Initialise the system
    system = md.initialise(2, 1, 31, 'square', timestep_length=5e-16,
                           constants=[a, b], forcefield=bond)
    system.cut_off = 30
    system.particles['xposition'] = [20e-10, 22e-10]
    system.particles['yposition'] = [20e-10, 22e-10]
    # This sets the sampling class
    sample_system = sample.Energy(system, size='small')
    # Start at time 0
    system.time = 0
    # Begin the molecular dynamics loop
    for i in range(0, 4000):
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
        if system.step % 10 == 0:
            sample_system.update(system)
    return system
