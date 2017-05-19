#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/ruiy/gnuradio/gr-ruiy/lib
export PATH=/home/ruiy/gnuradio/gr-ruiy/grc/lib:$PATH
export LD_LIBRARY_PATH=/home/ruiy/gnuradio/gr-ruiy/grc/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-ruiy 
