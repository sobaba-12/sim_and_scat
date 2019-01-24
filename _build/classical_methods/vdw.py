from pylj import md, sample

def simulation(temperature):
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
    system = md.initialise(20, temperature, 20, 'square')
    # This sets the sampling class
    sample_system = sample.JustCell(system)
    # Start at time 0
    system.time = 0
    # Begin the molecular dynamics loop
    for i in range(0, 1000):
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
