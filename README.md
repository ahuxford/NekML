# NekML

NekML is an efficient, Nek5000 interface for on-the-fly data transfer of Nek5000 solution data to Python-based modules. This repo was initially created for machine learning applications, hence the name: NekML. 

NekML is based on the application of the Fortran-Python repository **Forpy** (https://github.com/ylikx/forpy) but directly applied to Nek5000. For further clarification and just getting started with using Forpy before applying it to Nek5000, please check out https://github.com/ylikx/forpy.

Created by Aaron Huxford: ahuxford@umich.edu

## Getting Started

1. To do all the examples, you need to have Python 3.X (X = version) along with numpy, matplotlib, h5py, and pytorch modules. An Anaconda environment can be used, but follow the instructions at https://github.com/ylikx/forpy for details/troubleshooting.

2. Add the following USR and USR_LFLAGS lines to your local Nek5000 installation's **makenek** file, which is located within your local 'Nek5000/bin' directory.
```
USR+="NekML.o forpy_mod.o"

USR_LFLAGS+="`python3.X-config --ldflags`"
```
where X corresponds to the specific Python 3 version you have installed. An example editted **makenek** file for use with Python 3.6 is located within NekML's 'files' directory.

3. Copy the **forpy_mod.F90**, and **NekML.f** file from NekML's 'files' directory to your local Nek5000 installation's 'Nek5000/core/3rd_party' directory.

4. Whenever using NekML, a copy of the provided **makefile_usr.inc** file located in the 'files' directory and a copy of the directory 'NekML_PyMods' must both be located in the working directory you want to run Nek5000 from. For example, 'examples/save_h5py' contains **makefile_usr.inc** and the 'NekML_PyMods' directory.

- 'NekML_PyMods' and **NekML.f** are made to be customized by the user, based on the user's pythonic needs. The provided files are just placeholders to show simple examples of Nek5000 -> python transfers on the fly.

5. When you run "makenek" you may need to run it up to 3 times (i.e. makenek clean, makenek, makenek, makenek) to complete the compilation of Nek5000 with NekML. There's a compilation bug I never fixed, but it'll still work. I think it's something with the makefile_usr.inc file.

- p.s. I get a compilation bug when compiling with gfortran 4.8.5 regarding the c_loc procedure in forpy_mod.F90, but I think the issue doesn't exist for newer compiler versions.

## Examples

`save_h5py`
- This example follows the `ext_cyl` example included with Nek5000. Here, we actively pull a velocity field on-the-fly from Nek5000 and call a Python function that writes the field to a h5 file using the h5py python module.

`serial_train`
- This example follows the `ext_cyl` example included with Nek5000, but with an example on-the-fly training of a neural network. The goal of the network is to predict each node's y-velocity using only the local x-velocity as an input. The network is trained on-the-fly, using live simulation data from every timestep within the simulation.
- This example of on-the-fly training negates the large data space needed for saving every timestep's solution data, which would be needed for the conventional, post-simulation training of a neural network. 
- To visualize the model's loss versus epoch, run the provided "plotloss.py" script.

`parallel_train`
- This example follows the `ext_cyl` example included with Nek5000, but with an example on-the-fly training of a neural network. The goal of the network is to predict each node's y-velocity using only the local x-velocity as an input. The network is trained on-the-fly, using live simulation data from every timestep within the simulation.
- This example can be ran in a parallel Nek5000 simulation (i.e. using the command `nekbmpi ext_cyl 8`) using multiple cores. Each core handles a region of the spatial domain, so each core's Nek5000 results are used to train a separate neural network.
- To visualize the model's loss versus epoch, run the provided "plotloss.py" script. This generates a single figure using all the cores' results.
