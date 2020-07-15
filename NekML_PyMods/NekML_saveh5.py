#
# Python Modules for NekML
#
#-------------------------------------------------------------#
# example python function, save numpy array to .h5 file
#-------------------------------------------------------------#
def saveh5py(varsave, istep,fname):

    import h5py

    # save to h5 file
    if istep == 0:
        h5fu = h5py.File(fname+'.h5', 'w')
    else:
        h5fu = h5py.File(fname+'.h5', 'a')
    
    h5fu.create_dataset(str(istep)+'step', data=varsave)
    h5fu.close()

    return
#-------------------------------------------------------------#
# example function for on-the-fly neural network training
def onflytraining():

    return











