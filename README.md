# NekML

NekML is an efficient Nek5000 interface for on-the-fly transfer of Nek5000's data to Python-based modules for machine learning applications, since the most popular machine learning libraries (i.e. TensorFlow and PyTorch) are Python-based. 

One use of the interface is on-the-fly training of neural networks using live Nek5000 simulation data.

Aaron Huxford, Summer 2020

## Notes
NekML is currently for serial Nek5000 simulations only, but parallelism is being actively developed.

## Getting Started

1) Install Python 3.XX and pip3 install numpy and h5py. Avoid using an Anaconda environment as it will cause compilation bugs/issues to emerge.

2) Add the following USR and USR_LFLAGS lines to your local Nek5000 installation's "makenek" file within your local Nek5000's 'bin' directory.

USR+="NekML.o forpy_mod.o"

USR_LFLAGS+="`python3.X-config --ldflags`"

where X corresponds to the specific Python 3 version you have installed. An example editted makenek file for use with Python 3.6 is located within NekML's 'files' directory.

3) Copy the forpy_mod.F90 file from NekML's 'files' directory to your local Nek5000 installation's 'core/3rd_party' directory.

4) Whenever using NekML, a copy of the provided "makefile_usr.inc" file located in NekML's 'files' directory must be in the run's directory . For example, 'examples/ext_cyl' contains "makefile_usr.inc" because it is a Nek5000 run directory that uses NekML.


5) When you run "makenek" you'll need to run it twice to complete the compilation of Nek5000 with NekML.

## Examples

`save_h5py`
- This example follows the `ext_cyl` example included with Nek5000. Here, we actively pull a velocity field on-the-fly from Nek5000 and call a Python function that writes the field to a h5 file using h5py.
