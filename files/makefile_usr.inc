### makefile needed to build forpy and NEKML use ###

clean::
	@rm -rf forpy_mod.mod

$(OBJDIR)/forpy_mod.o   :$S/3rd_party/forpy_mod.F90;    $(FC) -c $(FL2) $< -o $@
$(OBJDIR)/NekML.o       :$S/3rd_party/NekML.f;          $(FC) -c $(FL2) $< -o $@
