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

class iqbal_gen_3_0(gr.hier_block2):
    """
    Args:
        mag, theta, dc_i, dc_q
    """
    def __init__(self, mag=0, theta=0, dc_i=0, dc_q=0):
        gr.hier_block2.__init__(
            self, "IQ Imbalance Generator 3.0",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )
        
        half_theta = theta/2;
        half_theta = half_theta*math.pi/180.0
        ##################################################
        # Parameters
        ##################################################
        self.mag = mag
        self.theta = theta
        self.dc_i = dc_i
        self.dc_q = dc_q
        self.half_theta = half_theta
        ##################################################
        # Blocks
        ##################################################
        self.blocks_complex_to_float = blocks.complex_to_float(1)
        self.blocks_float_to_complex = blocks.float_to_complex(1)

        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((math.cos(half_theta), ))
        self.blocks_multiply_const_vxx_1 = blocks.multiply_const_vff((-math.sin(half_theta), ))
        self.blocks_multiply_const_vxx_2 = blocks.multiply_const_vff((-math.sin(half_theta), ))
        self.blocks_multiply_const_vxx_3 = blocks.multiply_const_vff((math.cos(half_theta), ))

        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.blocks_add_xx_1 = blocks.add_vff(1)
        
        self.blocks_mag_0 = blocks.multiply_const_vff((1+mag, ))
        self.blocks_mag_1 = blocks.multiply_const_vff((1-mag, ))

        self.blocks_add_const_vxx_0 = blocks.add_const_vff((dc_i, ))
        self.blocks_add_const_vxx_1 = blocks.add_const_vff((dc_q, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self, 0), (self.blocks_complex_to_float, 0))
        self.connect((self.blocks_complex_to_float, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.blocks_complex_to_float, 0), (self.blocks_multiply_const_vxx_2, 0))
        self.connect((self.blocks_complex_to_float, 1), (self.blocks_multiply_const_vxx_1, 0))
        self.connect((self.blocks_complex_to_float, 1), (self.blocks_multiply_const_vxx_3, 0))

        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_2, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_multiply_const_vxx_3, 0), (self.blocks_add_xx_1, 1))


        self.connect((self.blocks_add_xx_0, 0), (self.blocks_mag_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.blocks_mag_1, 0))

        self.connect((self.blocks_mag_0, 0), (self.blocks_add_const_vxx_0, 0))
        self.connect((self.blocks_mag_1, 0), (self.blocks_add_const_vxx_1, 0))

        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_complex, 0))
        self.connect((self.blocks_add_const_vxx_1, 0), (self.blocks_float_to_complex, 1))

        self.connect((self.blocks_float_to_complex, 0), (self, 0))

