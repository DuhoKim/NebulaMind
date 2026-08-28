# URL: https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/

**Reproduction of asymmetry in HSC galaxies direction of rotation**

This page provides code and data for the reproduction of the analysis and results of the asymmetry observed in the distribution of galaxy direction of rotation.

The list of galaxy coordinates and the directions of rotation is available at [data.xlsx](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/data.xlsx). The file includes the directions of rotations of galaxies closer to the Southern Galactic pole and the Northern Galactic pole. It allows to observed the simple separation of galaxies by their direction of rotation relative to the rotation of the Earth within the Milky Way.

To observe the dipole axis, the code that should be used is:
[dipole.cpp](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/dipole.cpp).

Since the simulation requires substantial computing time, it is written in C.

To compile the code type: g++ -o dipole dipole.cpp

The input data is in the file [data\_hsc.csv](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/data_hsc.csv). That is the exact same galaxies in the file data.xlsx above, but in a single list.

To run the code on the data type: ./dipole data\_hsc.csv

The program will print the results in the standard output. The program takes several hours to run.

The output of applying the code to the data is in the file [hsc\_results\_all.csv](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/hsc_results_all.csv). It shows the probability (sigma) of a dipole axis to form by chance from each location in the sky. It is important to remember that because the simulation is done by comparing the real directions to random directions, every time the code runs the results will be slightly different. Your output will therefore not be identical to the example output above, but it will be very close.

![](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/hsc_results_all.jpg)

A visualization of the results ( [hsc\_results\_all.csv](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/hsc_results_all.csv)) using Mollweide projection.

## Repeating the experiment with random spin directions

To ensure that the results are consistent, the experiment can be repeated with the exact same code but when the galaxies are assigned with random spin directions. The file [hsc\_random.csv](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/hsc_random.csv) contains the exact same galaxies, but each galaxy is assigned with a random spin direction.

To run the code on the data type: ./dipole hsc\_random.csv

The program will run exactly like when the spin directions are the real spin directions, but with random spin directions.

The output of applying the code to the data is in the file [hsc\_random\_results.csv](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/hsc_random_results.csv).

![](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/hsc_random_results.jpg)

A Mollweide visualization of the results ( [hsc\_random\_results.csv](https://people.cs.ksu.edu/~lshamir/data/asymmetry_hsc/hsc_random_results.csv)) when the galaxy spin directions are random.