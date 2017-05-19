#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/ruiy/gnuradio/gr-ruiy/python
export PATH=/home/ruiy/gnuradio/gr-ruiy/grc/python:$PATH
export LD_LIBRARY_PATH=/home/ruiy/gnuradio/gr-ruiy/grc/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/ruiy/gnuradio/gr-ruiy/grc/swig:$PYTHONPATH
/usr/bin/python2 /home/ruiy/gnuradio/gr-ruiy/python/qa_iqbal_gen_2_0.py 
