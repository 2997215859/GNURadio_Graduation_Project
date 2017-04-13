#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Copyright 2017 <+YOU OR YOUR COMPANY+>.
# 
# This is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this software; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

import numpy
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
import math


class iqbal_gen_2_0(gr.hier_block2):
    """
    Args:
        mag,phase,c,d
        a + b * i => a * mag + c + (a * sin(phase) + b + d) * i
    """
    def __init__(self, magnitude=0,phase=0,c=0,d=0):
        gr.hier_block2.__init__(
            self, "IQ Imbalance Generator",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.magnitude = magnitude
        self.phase = phase
        self.c = c
        self.d = d
        ##################################################
        # Blocks
        ##################################################
        self.mag = blocks.multiply_const_vff((math.pow(10,magnitude/20.0), ))
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((math.sin(phase*math.pi/180.0), ))
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff((c, ))
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((d, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_float_to_complex_0, 0), (self, 0))
        self.connect((self, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.mag, 0))
        self.connect((self.mag, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_complex_0, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.blocks_add_const_vxx_1, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_float_to_complex_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_complex_to_float_0, 0), (self.blocks_multiply_const_vxx_0, 0))


# QT sink close method reimplementation

    def get_magnitude(self):
        return self.magnitude

    def set_magnitude(self, magnitude):
        self.magnitude = magnitude
        self.mag.set_k((math.pow(10,self.magnitude/20.0), ))

    def get_phase(self):
        return self.phase

    def set_phase(self, phase):
        self.phase = phase
        self.blocks_multiply_const_vxx_0.set_k((math.sin(self.phase*math.pi/180.0), ))



#    def work(self, input_items, output_items):
#       in0 = input_items[0]
#        out = output_items[0]
#        # <+signal processing here+>
#        out[:] = in0
#        return len(output_items[0])

