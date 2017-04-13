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
from math import pi, log
from cmath import exp

from gnuradio.digital.generic_mod_demod import generic_mod
import numpy
from gnuradio import gr
import gnuradio.digital.digital_swig as digital_swig
from gnuradio.digital.bpsk import bpsk_mod
from gnuradio.digital.qpsk import qpsk_mod
from gnuradio.digital.utils import mod_codes, gray_code

from gnuradio import blocks
from gnuradio import analog
try:
    from gnuradio import filter
except ImportError:
    import gnuradio.digital.filter_swig as filter
# The default encoding (e.g. gray-code, set-partition)
_def_mod_code = mod_codes.GRAY_CODE
_def_excess_bw = 0.35
_def_constellation_points = 4
_def_differential = True
_def_samples_per_symbol = 2
_def_sensitivity = 1
_def_bt = 0.35
_def_verbose = False
_def_log = False
# gr.sync_block
def create_encodings(mod_code, arity, differential):
    post_diff_code = None
    if mod_code not in mod_codes.codes:
        raise ValueError('That modulation code does not exist.')
    if mod_code == mod_codes.GRAY_CODE:
        if differential:
            pre_diff_code = gray_code.gray_code(arity)
            post_diff_code = None
        else:
            pre_diff_code = []
            post_diff_code = gray_code.gray_code(arity)
    elif mod_code == mod_codes.NO_CODE:
		pre_diff_code = []
		post_diff_code = None
    else:
        raise ValueError('That modulation code is not implemented for this constellation.')
    return (pre_diff_code, post_diff_code)

def psk_constellation(m=_def_constellation_points, mod_code=_def_mod_code, differential=_def_differential):
    """
    Creates a PSK constellation object.
    """
    k = log(m) / log(2.0)
    if (k != int(k)):
        raise StandardError('Number of constellation points must be a power of two.')
    points = [exp(2*pi*(0+1j)*i/m) for i in range(0,m)]
    pre_diff_code, post_diff_code = create_encodings(mod_code, m, differential)
    if post_diff_code is not None:
        inverse_post_diff_code = mod_codes.invert_code(post_diff_code)
        points = [points[x] for x in inverse_post_diff_code]
    constellation = digital_swig.constellation_psk(points, pre_diff_code, m)
    return constellation

class mul_mod(generic_mod):
    """
    docstring for block mul_mod

    args for bpsk:
        Hierarchical block for RRC-filtered BPSK modulation.

        The input is a byte stream (unsigned char) and the
        output is the complex modulated signal at baseband.

        Args:
            mod_code: Argument is not used.  It exists purely to simplify generation of the block in grc.
            differential: Whether to use differential encoding (boolean).
 


    args for qpsk:
        Hierarchical block for RRC-filtered QPSK modulation.

        The input is a byte stream (unsigned char) and the
        output is the complex modulated signal at baseband.

        Args:
            mod_code: Whether to use a gray_code (digital.mod_codes.GRAY_CODE) or not (digital.mod_codes.NO_CODE).
            differential: Whether to use differential encoding (boolean).
 

    args for psk:
        Hierarchical block for RRC-filtered PSK modulation.

        The input is a byte stream (unsigned char), treated as a series of packed symbols. Symbols are grouped from MSB to LSB.
        The output is the complex modulated signal at baseband, with a given number of samples per symbol.
        If "Samples/Symbol" is 2, and "Number of Constellation Points" is 4, a single byte contains four symbols, and will produce eight samples.

        Args:
            constellation_points: Number of constellation points (must be a power of two) (integer).
            mod_code: Whether to use a gray_code (digital.mod_codes.GRAY_CODE) or not (digital.mod_codes.NO_CODE).
            differential: Whether to use differential encoding (boolean).


    args for gfsk:
        Hierarchical block for Gaussian Frequency Shift Key (GFSK) modulation.

        The input is a byte stream (unsigned char) and the output is the complex modulated signal at baseband.

        Args:
            samples_per_symbol: samples per baud >= 2 (integer)
            bt: Gaussian filter bandwidth * symbol time (float)
            verbose: Print information about modulator? (bool)
            debug: Print modualtion data to files? (bool)


    args for gmsk:
        Hierarchical block for Gaussian Minimum Shift Key (GMSK) modulation.

        The input is a byte stream (unsigned char with packed bits) and the output is the complex modulated signal at baseband.

        Args:
            samples_per_symbol: samples per baud >= 2 (integer)
            bt: Gaussian filter bandwidth * symbol time (float)
            verbose: Print information about modulator? (boolean)
            log: Print modulation data to files? (boolean)

    """
    def __init__(self, mod_type, mod_code=_def_mod_code, differential=False,
                 excess_bw=_def_excess_bw, sensitivity=_def_sensitivity, bt=_def_bt,
                 verbose=_def_verbose, log=_def_log, samples_per_symbol=_def_samples_per_symbol):
        if mod_type == "bpsk":
            constellation = digital_swig.constellation_bpsk()
            super(mul_mod, self).__init__(constellation=constellation, differential=differential)

        if mod_type == "qpsk":
            # here "qpsk" be just different from "4psk" later by phase 
            pre_diff_code = True 
            if not differential:
                constellation = digital_swig.constellation_qpsk()
                if mod_code != mod_codes.GRAY_CODE:
                    raise ValueError("This QPSK mod/demod works only for gray-coded constellations.")
            else:
                constellation = digital_swig.constellation_dqpsk()
                if mod_code not in set([mod_codes.GRAY_CODE, mod_codes.NO_CODE]):
                    raise ValueError("That mod_code is not supported for DQPSK mod/demod.")
                if mod_code == mod_codes.NO_CODE:
                    pre_diff_code = False
            super(mul_mod, self).__init__(constellation=constellation, differential=differential,
                                          pre_diff_code=pre_diff_code, excess_bw=excess_bw)
        if mod_type == "psk":
            constellation = psk_constellation(_def_constellation_points, mod_code, differential)
            super(mul_mod, self).__init__(constellation, differential, samples_per_symbol=_def_samples_per_symbol, excess_bw=excess_bw)

        if mod_type == "gfsk":
            gr.hier_block2.__init__(self, "gfsk_mod",
				gr.io_signature(1, 1, gr.sizeof_char),       # Input signature
				gr.io_signature(1, 1, gr.sizeof_gr_complex)) # Output signature).
            samples_per_symbol = int(samples_per_symbol)
            self._samples_per_symbol = samples_per_symbol
            self._bt = bt
            self._differential = False

            if not isinstance(samples_per_symbol, int) or samples_per_symbol < 2:
                raise TypeError, ("samples_per_symbol must be an integer >= 2, is %r" % (samples_per_symbol,))

            ntaps = 4 * samples_per_symbol			# up to 3 bits in filter at once
            #sensitivity = (pi / 2) / samples_per_symbol	# phase change per bit = pi / 2

            # Turn it into NRZ data.
            #self.nrz = digital.bytes_to_syms()
            self.unpack = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
            self.nrz = digital_swig.chunks_to_symbols_bf([-1, 1])

            # Form Gaussian filter
            # Generate Gaussian response (Needs to be convolved with window below).
            self.gaussian_taps = filter.firdes.gaussian(1.0, # gain
                                                        samples_per_symbol,    # symbol_rate
                                                        bt,  # bandwidth * symbol time
                                                        ntaps              # number of taps
                                                       )

            self.sqwave = (1,) * samples_per_symbol       # rectangular window
            self.taps = numpy.convolve(numpy.array(self.gaussian_taps),numpy.array(self.sqwave))
            self.gaussian_filter = filter.interp_fir_filter_fff(samples_per_symbol, self.taps)

            # FM modulation
            self.fmmod = analog.frequency_modulator_fc(sensitivity)

            # small amount of output attenuation to prevent clipping USRP sink
            self.amp = blocks.multiply_const_cc(0.999)

            if verbose:
                self._print_verbage()

            if log:
                self._setup_logging()

            # Connect & Initialize base class
            self.connect(self, self.unpack, self.nrz, self.gaussian_filter, self.fmmod, self.amp, self)

        if  mod_type == "gmsk":
            gr.hier_block2.__init__(self, "gmsk_mod",
			gr.io_signature(1, 1, gr.sizeof_char),       # Input signature
			gr.io_signature(1, 1, gr.sizeof_gr_complex)) # Output signature

            samples_per_symbol = int(samples_per_symbol)
            self._samples_per_symbol = samples_per_symbol
            self._bt = bt
            self._differential = False

            if not isinstance(samples_per_symbol, int) or samples_per_symbol < 2:
                raise TypeError, ("samples_per_symbol must be an integer >= 2, is %r" % (samples_per_symbol,))

            ntaps = 4 * samples_per_symbol			# up to 3 bits in filter at once
            sensitivity = (pi / 2) / samples_per_symbol	# phase change per bit = pi / 2

            # Turn it into NRZ data.
            #self.nrz = digital.bytes_to_syms()
            self.unpack = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
            self.nrz = digital_swig.chunks_to_symbols_bf([-1, 1], 1)

            # Form Gaussian filter
            # Generate Gaussian response (Needs to be convolved with window below).
            self.gaussian_taps = filter.firdes.gaussian(1, # gain
                                                        samples_per_symbol,    # symbol_rate
                                                        bt,      # bandwidth * symbol time
                                                        ntaps              # number of taps
                                                       )
            self.sqwave = (1,) * samples_per_symbol       # rectangular window
            self.taps = numpy.convolve(numpy.array(self.gaussian_taps),numpy.array(self.sqwave))
            self.gaussian_filter = filter.interp_fir_filter_fff(samples_per_symbol, self.taps)
            # FM modulation
            self.fmmod = analog.frequency_modulator_fc(sensitivity)
            if verbose:
                self._print_verbage()

            if log:
                self._setup_logging()
            # Connect & Initialize base class
            self.connect(self, self.unpack, self.nrz, self.gaussian_filter, self.fmmod, self)


#    def work(self, input_items, output_items):
#        in0 = input_items[0]
#        out = output_items[0]
#        # <+signal processing here+>
#        out[:] = in0
#        return len(output_items[0])

