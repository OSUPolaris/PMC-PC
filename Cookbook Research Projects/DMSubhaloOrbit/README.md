# Title: Falling Through the Dark: Subhalo Orbits in Cold and Self-Interacting Dark Matter Halos
Original Author: Chloe Zheng

*Subfield: Astrophysics*

*Topics covered: Cold Dark matter, Self-Interacting Dark matter, orbital dynamics, N-body simulations*

*Type of project: Computational*

## Short Description:
In this project, the student will learn the basics of dark matter and how a small dark matter halo (a subhalo) orbits inside a much larger (and heavier) host halo. First, the student will read introductory material on cold dark matter (CDM), its small-scale challenges, and self-interacting dark matter (SIDM). Next, the student will learn to read simulation data stored in HDF5 files and make 3D visualizations of the host and subhalo initial conditions. The student will then generate a table of the NFW host halo’s density, enclosed mass, and velocity profiles, which is used as input for the N-body simulations. Using the Python package galpy, the student will integrate the predicted orbit of the subhalo in an analytic NFW potential. Once CDM and SIDM simulations are ready, the student will extract the subhalo’s trajectory from halo finder (AHF) catalogs and compare the simulated orbits against the prediction, including orbital radius versus time, pericenter, apocenter, and orbital period. Finally, the student will measure how the subhalo itself changes along its orbit, through its density profile, mass loss, and velocity dispersion, and compare how CDM and SIDM subhalos evolve. Time permitting, the student may integrate orbits in a realistic host potential built from simulation-derived M(<r), or look at energy, angular momentum, and radial phase space (r, v_r).

## Materials
Project files can be found at https://github.com/xchloezheng/subhalo_orbits_project.
