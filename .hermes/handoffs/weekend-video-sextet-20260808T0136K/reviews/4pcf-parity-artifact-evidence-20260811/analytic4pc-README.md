# Analytic4PC
Julia code to calculate the “analytic 4-point covariance” defined in [arXiv:2108.01714][1] and used in [arXiv:2206.03625][2], [arXiv:2206.04227][3]. The core functions for the covariance calculation are in the separate package [AnalyticCovariance.jl](https://gitlab.com/Socob/AnalyticCovariance.jl).


## Installation
All required packages should be installed automatically when the code is run. In order to trigger this step manually (e. g. to prepare for non-interactive runs), you can also simply run
```
./analytic4pc-run --help
```
(within the repository directory).


## Running
The main program is [`analytic4pc-run`](analytic4pc-run), which calculates parity-odd covariance matrix elements and writes the result to a file `cov.jld2` in [JLD2](https://github.com/JuliaIO/JLD2.jl) (based on HDF5) format. There is also the script [`npcf_cov_run.py`](test/npcf_cov_run.py), which runs the Python code from [arXiv:2108.01714][1] instead.

Information about command line arguments can be retrieved using `analytic4pc-run --help`. For example, to calculate the full parity-odd 10-bin NGC covariance from [arXiv:2206.04227][3] using default numerical parameters:
```
./analytic4pc-run \
	--power-spectrum pk_patchy_eft_fit_tempered.npy \
	--shot-noise 3134.796238244514Mpc^3 --volume 1.9Gpc^3 \
	--r-bins \
		 20Mpc,34Mpc  \
		 34Mpc,48Mpc  \
		 48Mpc,62Mpc  \
		 62Mpc,76Mpc  \
		 76Mpc,90Mpc  \
		 90Mpc,104Mpc \
		104Mpc,118Mpc \
		118Mpc,132Mpc \
		132Mpc,146Mpc \
		146Mpc,160Mpc \
	--r-max 1000Mpc --Nr 4100 \
	--k-max   5/Mpc --Nk 5000 \
	--k-window-function 'exp(-(k * Mpc)^2)' \
	--integ-bessel-threshold 1.0 1.0 1.0 1.0 1.0 \
	--integ-bessel-N 7
```
(the arguments `--r-max`, `--Nr`, `--k-max`, `--Nk`, `--k-window-function`, `--integ-bessel-threshold`, and `--integ-bessel-N` can also be omitted to use these default values).


### Running in parallel on a single machine
When running on a single machine, the simplest way to get parallel computation is to use Julia’s `-p` option:
```
julia -p 8 analytic4pc-run --power-spectrum pk_patchy_eft_fit_tempered.npy ...
```
will run on 8 cores.


### Running in parallel on a computing cluster
For running on a cluster (e. g. Symmetry), there is the run script `analytic4pc-run-slurm` for use with SLURM that uses as many cores as provided in the SLURM allocation. There are also some example job scripts in the [`job-scripts/`](job-scripts/) folder (making use of `analytic4pc-run`) which have some sets of input parameters pre-defined, e. g.
```
sbatch --nodes=4 --ntasks-per-node=40 job-scripts/symmetry-slurm.sh \
	2206.03625/CMASS-NGC/18 \
	--Nr 4100 ...
```
to calculate the parity-odd 18-bin CMASS NGC covariance from [arXiv:2206.03625][2] on 160 cores.


### Console/log output
The code shows a progress bar in the console. When console output is redirected to a file (e. g. on a computing cluster with a scheduler like SLURM), this can create a mess when the file is shown in a text file viewer/editor (e. g. `less`), since that will show the “raw” characters in the file instead of repeatedly moving the cursor back and overwriting the output like in the console. In order to view the log file like it would have shown in the console,
```
tail -f log.txt
```
(for continuous updates) or
```
cat log.txt
```
(for a single view of the current state) can be used.


## Loading results
The JLD2 format retains the type information of Julia objects, so that the result from loading the file is identical to the variables when the file was written. The drawback of this is that it’s less straightforward to load the data from other programming languages.

All packages which define types used in the output (including external packages) must be loaded at the time when the file is read again:
```
using FileIO, EndpointRanges, OffsetArrays, Unitful, UnitfulAstro
data = load("cov.jld2")
```


## Output format
As mentioned above, the output file format is JLD2 (which is based on HDF5). Since the Python code [arXiv:2108.01714][1] uses a somewhat idiosyncratic output format (a Python pickled dictionary object, where the covariance’s l indices are used to select β-indexed sub-matrices), both the “normal” covariance matrix and this dictionary-based format are provided, including conversion between the two.

Specifically, the JLD2 output dataset `covariance` is the full covariance matrix, with the dataset `matrix_indices` specifying how the integer matrix indices map to the estimator’s six indices (l₁, l₂, l₃, β₁, β₂, β₃) (i. e. two sets are selected per covariance matrix element – one each for both axes). On the other hand, `covariance_dict` is a dictionary like in the Python code. Given one of these dictionaries, the function `cov_dict_to_matrix` (in [`dict-to-matrix.jl`](dict-to-matrix.jl); load via `include("dict-to-matrix.jl")`) can be used to construct the covariance matrix from a dictionary and also returns the corresponding map from matrix axis to estimator indices.

Finally, the script [`tools/jld2-to-pkl.jl`](tools/jld2-to-pkl.jl) (see `jld2-to-pkl.jl --help`) converts a JLD2 output file to the equivalent Python pickle `.cov` file for compatibility with the Python code’s output. For convenience, the covariance matrix is included in the dictionary under the key `cov['attrs']['covariance_matrix']` (this field is not present in the Python code’s output).


[1]: https://arxiv.org/abs/2108.01714
[2]: https://arxiv.org/abs/2206.03625
[3]: https://arxiv.org/abs/2206.04227
