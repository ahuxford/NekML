def saveh5py(varsave, istep,fname):

    import numpy as np
    import h5py

    # save to h5 file
    if istep == 0:
        h5fu = h5py.File(fname+'.h5', 'w')
    else:
        h5fu = h5py.File(fname+'.h5', 'a')
    
    h5fu.create_dataset(str(istep)+'step', data=varsave)
    h5fu.close()

    return
