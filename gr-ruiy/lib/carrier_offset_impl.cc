/* -*- c++ -*- */
/* 
 * Copyright 2017 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "carrier_offset_impl.h"
#include <math.h>
namespace gr {
  namespace ruiy {

    carrier_offset::sptr
    carrier_offset::make(float df_f0_ratio)
    {
      return gnuradio::get_initial_sptr
        (new carrier_offset_impl(df_f0_ratio));
    }

    /*
     * The private constructor
     */
    carrier_offset_impl::carrier_offset_impl(float df_f0_ratio)
      : gr::block("carrier_offset",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))),
      d_df_f0_ratio(df_f0_ratio)
    {}

    /*
     * Our virtual destructor.
     */
    carrier_offset_impl::~carrier_offset_impl()
    {
    }

    void
    carrier_offset_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
        unsigned ninputs = ninput_items_required.size();
        for(unsigned i=0;i<ninputs;i++){
            ninput_items_required[i] = noutput_items;
        }
    }

    int
    carrier_offset_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
      const gr_complex *in = (gr_complex*) input_items[0];
      gr_complex *out = (gr_complex*) output_items[0];

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);
      int base_num = nitems_written(0);
      for(int i=0;i<noutput_items;i++){
          int n = base_num + i;
          out[i] = in[i] * gr_complex(cos(2*M_PI*n*d_df_f0_ratio), -sin(2*M_PI*n*d_df_f0_ratio));
      }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace ruiy */
} /* namespace gr */

