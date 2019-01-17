# The interaction between simulation and scattering

**Classical molecular dynamics** (MD) is a common computational chemistry technique for studying complex systems, such as proteins, polymers, and battery materials {% cite karplus_molecular_2002 binder_monte_1995 kim_effect_2011 burbano_sparse_2016%}. Alongside the interest in these and other applications, molecular dynamics is also a used to help analyse data obtained from elastic scattering instruments.

This tutorial has been written to **introduce users of elastic-scattering techniques**, such as small angle scattering or diffraction, to classical molecular dynamics (MD) simulation. We hope that this tutorial can provide an accessible route for experimental researchers to **better understand some of the complexities and subtleties of MD simulation**, thereby helping these researchers to get more relevant information from their simulations.

This tutorial begins with an introduction to classical simulation methods, including a discussion of the development and parameterisation of classical interatomic potential models. We then provide an outline of traditional molecular dynamics simulation methods and discuss a number of important considerations users of MD simulation should be aware of. We close this tutorial with an illustrative practical example, using the open-source Lennard-Jones simulation package [`pylj`](http://pythoninchemistry.org/pylj) {% cite mccluskey_pylj_2018 mccluskey_arm61/pylj_2018 %}, and discuss how a radially averaged scattering profile may be obtained **directly from simulation** via the Debye equation {% cite debye_zerstreuung_1915 %}.

We wish to emphasise that this tutorial is in **no way** a complete course on molecular dynamics, and would direct the interested reader to one of the many detailed textbooks on this subject {% cite harvey_computational_2018 grant_computational_1995 leach_molecular_1996 frenkel_understanding_1996 allen_computer_2017 %}. Rather, it is our hope that this tutorial provides a simple, practical, **general introduction to new, or future, users of MD methods within the scattering community**.

## References 

{% bibliography --cited %}
