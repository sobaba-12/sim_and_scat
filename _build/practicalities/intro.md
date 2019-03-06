---
title: 'Practicalities'
prev_page:
  url: /calculating_scattering/scaling
  title: 'Scaling'
next_page:
  url: /practicalities/visualise
  title: 'Visualise the simulation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Practicalities

While it is important to understand the fundamentals and underlying mechanics, we are really interested in using molecular dynamics as a tool for analysis.
Now, let us look at a "real" molecular dynamics simulation and see how we can quickly and easily compare it with experimental data.
This will not be a in depth look into the intricacies of modelling experimental data, instead we will focus on how to quickly compare a simulation to an experiment.  

The example we will use is that of the protein lysozyme in water, we choose this as there exists already a [great tutorial](http://www.mdtutorials.com/gmx/lysozyme/index.html) from Justin Lemkul on how to simulate this system and experimental data is available on the [SASBDB](https://www.sasbdb.org/data/SASDA96/).
We have included in the GitHub repository for this resource a pdb format trajectory of a lysozyme protein in water that can be used in the next stages.
However, if you would like to generate your own feel free to work through Justin's tutorial and return to this (if you do this you will need to [convert](http://manual.gromacs.org/archive/5.0.5/programs/gmx-trjconv.html) the production simulation to a pdb format). 
