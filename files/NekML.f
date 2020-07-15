c---------------------------------------------------------------------
c NekML
c
c Interface for Nek5000 machine learning (ML) applications.
c
c---------------------------------------------------------------------

c---------------------------------------------------------------------
c NekML_test
c
c test subroutine
c
c---------------------------------------------------------------------
      subroutine NekML_test

      use forpy_mod

      include 'SIZE'
      include 'SOLN'
      include 'TSTEP'
    
      integer         :: ierror,Nuse
      type(tuple)     :: args1
      type(module_py) :: mymodule
      type(list)      :: paths
      type(ndarray)   :: arr_ux, arr_uy

c     start NekML portion

      ierror = forpy_initialize()
      ierror = ndarray_create(arr_ux, vx)
      ierror = ndarray_create(arr_uy, vy)

c     add the current directory "." to PYTHONPATH
      ierror = get_sys_path(paths)
      ierror = paths%append(".")

c     import python function
      ierror = import_py(mymodule, "save_h5py")
      
c     set arguments 
      ierror = tuple_create(args1, 4)
      ierror = args1%setitem(0, arr_ux)
      ierror = args1%setitem(1, arr_uy)
      ierror = args1%setitem(2, istep)
      Nuse   = 0
      ierror = args1%setitem(3, Nuse)

      if (mod(istep,200) == 0) then
          ierror = call_py_noret(mymodule, "saveh5py",args1)
          Nuse = Nuse + 1
      end if

c     end NekML portion

      write(*,*) "in NekML_test"

      end
