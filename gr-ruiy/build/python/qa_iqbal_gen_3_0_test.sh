#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/ruiy/gnuradio/gr-ruiy/python
export PATH=/home/ruiy/gnuradio/gr-ruiy/build/python:$PATH
export LD_LIBRARY_PATH=/home/ruiy/gnuradio/gr-ruiy/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/ruiy/gnuradio/gr-ruiy/build/swig:$PYTHONPATH
/usr/bin/python2 /home/ruiy/gnuradio/gr-ruiy/python/qa_iqbal_gen_3_0.py 
