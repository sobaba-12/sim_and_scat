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
        return -constants[0] * (np.abs(dr) - constants[1])
    else:
        return constants[0] / 2. * np.power((dr - constants[1]), 2)

def simulation(temperature):
    """
    Runs a molecular dynamics simulation in suing the pylj molecular dynamics engine.

    Parameters
    ----------
    temperature: float
        The temperature for the initialisation and thermostating

    Returns
    -------
    pylj.util.System
        The complete system information from pylj
    """
    # Initialise the system
    system = md.initialise(2, temperature, 10, 'square',
                           constants=[440.5, 1.522e-10], forcefield=bond)
    system.cut_off = 30
    system.particles['xposition'] = [5e-10, 6e-10]
    system.particles['yposition'] = [5e-10, 6e-10]
    # This sets the sampling class
    sample_system = sample.JustCell(system, scale=2)
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
