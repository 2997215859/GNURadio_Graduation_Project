/* -*- c++ -*- */

#define RUIY_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "ruiy_swig_doc.i"

%{
#include "ruiy/carrier_offset.h"
%}


%include "ruiy/carrier_offset.h"
GR_SWIG_BLOCK_MAGIC2(ruiy, carrier_offset);

