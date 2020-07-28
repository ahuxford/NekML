# NekML

NekML is an efficient Nek5000 interface for on-the-fly transfer of Nek5000's data to Python-based modules for machine learning applications, since the most popular machine learning libraries (i.e. TensorFlow and PyTorch) use Python APIs. 

One use of the interface is on-the-fly, serial or parallel training of neural networks using live Nek5000 simulation data.

Created by Aaron Huxford: ahuxford@umich.edu

## Getting Started

1. Install Python 3.X along with the numpy, matplotlib, h5py, and pytorch modules. Avoid using an Anaconda environment as it will cause compilation bugs.

2. Add the following USR and USR_LFLAGS lines to your local Nek5000 installation's **makenek** file, which is located within your local Nek5000's 'bin' directory.
```
USR+="NekML.o forpy_mod.o"

USR_LFLAGS+="`python3.X-config --ldflags`"
```
where X corresponds to the specific Python 3 version you have installed. An example editted **makenek** file for use with Python 3.6 is located within NekML's 'files' directory.

3. Copy the **forpy_mod.F90** file from NekML's 'files' directory to your local Nek5000 installation's 'core/3rd_party' directory.

4. Whenever using NekML, a copy of the provided **makefile_usr.inc** file that is located in NekML's 'files' directory  and a copy of the directory 'NekML_PyMods' must both be in the directory you want to run Nek5000 in. For example, 'examples/save_h5py' contains **makefile_usr.inc** and 'NekML_PyMods'.

5. When you run "makenek" you may need to run it up to 3 times (i.e. run make clean, makenek, makenek, makenek) to complete the compilation of Nek5000 with NekML. There's a compilation bug that's a minor inconvenience.

## Examples

`save_h5py`
- This example follows the `ext_cyl` example included with Nek5000. Here, we actively pull a velocity field on-the-fly from Nek5000 and call a Python function that writes the field to a h5 file using h5py.

`serial_train`
- This example follows the `ext_cyl` example included with Nek5000, but with an example on-the-fly training of a neural network. The goal of the network is to predict each node's y-velocity using only the local x-velocity as an input. The network is trained on-the-fly, using live simulation data from every timestep within the simulation.
- This example of on-the-fly training negates the large data space needed for saving every timestep's solution data, which would be needed for the conventional, post-simulation training of a neural network. 
- To visualize the model's loss versus epoch, run the provided "plotloss.py" script.

`parallel_train`
- This example follows the `ext_cyl` example included with Nek5000, but with an example on-the-fly training of a neural network. The goal of the network is to predict each node's y-velocity using only the local x-velocity as an input. The network is trained on-the-fly, using live simulation data from every timestep within the simulation.
- This example can be ran in a parallel Nek5000 simulation (i.e. using the command `nekbmpi ext_cyl 8`) using multiple cores. Each core handles a region of the spatial domain, so each core's Nek5000 results are used to train a separate neural network.
- To visualize the model's loss versus epoch, run the provided "plotloss.py" script. This generates a single figure using all the cores' results.
