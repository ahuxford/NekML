c---------------------------------------------------------------------
c NekML
c
c Interface for Nek5000 machine learning (ML) applications.
c
c---------------------------------------------------------------------
c NekML_savevx2h5
c
c save vx to a .h5 file, serves as an example for than anything
c - to modify, just change ndarray_create(arr,___) variable
c - change args1%setitem(2, "___") string
c
c---------------------------------------------------------------------
      subroutine NekML_savevx2h5(isaveh5)

      use forpy_mod
      include 'SIZE'
      include 'SOLN'
      include 'TSTEP'
    
      integer         :: ierror
      type(tuple)     :: args1
      type(module_py) :: mymodule
      type(list)      :: paths
      type(ndarray)   :: arr

      ierror = forpy_initialize()
      ierror = ndarray_create(arr,vx)
c add directory with NekML Python modules to PYTHONPATH
      ierror = get_sys_path(paths)
      ierror = paths%append("NekML_PyMods")
      ierror = import_py(mymodule, "NekML")

c set arguments 
      ierror = tuple_create(args1, 3)
      ierror = args1%setitem(0, arr)
      ierror = args1%setitem(1, istep)
      ierror = args1%setitem(2, "vx")


      ierror = call_py_noret(mymodule, "saveh5py",args1)

      call args1%destroy
      
      end
c---------------------------------------------------------------------
c NekML_serialtrain
c
c save vx to a .h5 file, serves as an example for than anything
c - to modify, just change ndarray_create(arr,___) variable
c - change args1%setitem(2, "___") string
c
c---------------------------------------------------------------------
      subroutine NekML_serialtrain()

      use forpy_mod
      include 'SIZE'
      include 'SOLN'
      include 'TSTEP'
    
      integer         :: ierror
      type(tuple)     :: args1
      type(module_py) :: mymodule
      type(list)      :: paths
      type(ndarray)   :: arr_in, arr_out

      ierror = forpy_initialize()

      ierror = ndarray_create(arr_in,vx)  !  input of neural network
      ierror = ndarray_create(arr_out,vy) ! output of neural network

c add directory with NekML Python modules to PYTHONPATH
      ierror = get_sys_path(paths)
      ierror = paths%append("NekML_PyMods")
      ierror = import_py(mymodule, "NekML")

c set arguments 
      ierror = tuple_create(args1, 3)
      ierror = args1%setitem(0, arr_in)
      ierror = args1%setitem(1, arr_out)
      ierror = args1%setitem(2, istep)

      ierror = call_py_noret(mymodule, "serial_train",args1)

      call args1%destroy
      
      end
