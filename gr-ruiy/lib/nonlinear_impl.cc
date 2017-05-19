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
#include "nonlinear_impl.h"

namespace gr {
  namespace ruiy {

    nonlinear::sptr
    nonlinear::make(bool is_nonlinear)
    {
      return gnuradio::get_initial_sptr
        (new nonlinear_impl(is_nonlinear));
    }

    /*
     * The private constructor
     */
    nonlinear_impl::nonlinear_impl(bool is_nonlinear)
      : gr::block("nonlinear",
              gr::io_signature::make(1, 1, sizeof(gr_complex)),
              gr::io_signature::make(1, 1, sizeof(gr_complex))),
	d_is_nonlinear(is_nonlinear)
    {}

    /*
     * Our virtual destructor.
     */
    nonlinear_impl::~nonlinear_impl()
    {
    }

    void
    nonlinear_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      /* <+forecast+> e.g. ninput_items_required[0] = noutput_items */
    }


    gr_complex nonlinear_impl::complex_power(gr_complex b, int num)
    {
	    gr_complex res = 1;
    	    for(int i=0;i<num;i++){
    		    res = res * b;
    	    }
    	    return res;
    }

    gr_complex nonlinear_impl::complex_mul(gr_complex a, gr_complex b){
    	return gr_complex(a.real() * b.real() - a.imag() * b.imag(), a.real() * b.imag() + b.real() * a.imag());
    }
    int
    nonlinear_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
	    
	    
      const gr_complex *x = (const gr_complex *) input_items[0];
      gr_complex *y = (gr_complex *) output_items[0];

      // Do <+signal processing+>
      // Tell runtime system how many input items we consumed on
      // each input stream.
      consume_each (noutput_items);

      if(d_is_nonlinear == false){
	      for(int i=0;i<noutput_items;i++){
		      y[i] = x[i];
 	      }
	      return noutput_items;
      }


      for(int i=0;i<5;i++){
	      y[i] = x[i];
      }
      for(int i=5;i<noutput_items;i++){
	      y[i] = complex_mul(0.9, x[i]) + 
		     complex_mul(0.1, x[i-1]) + 
		     complex_mul(0.09, x[i-2]) + 
		     complex_mul(0.08, x[i-3]) + 
		     complex_mul(0.05, x[i-4]) + 
		     complex_mul(0.03, x[i-5]) + 
		     complex_mul(0.013, complex_mul(x[i], x[i-1])) + 
		     complex_mul(0.012, complex_mul(x[i], x[i-2])) + 
		     complex_mul(0.01, complex_mul(x[i], x[i-3])) + 
		     complex_mul(0.02, complex_mul(x[i], x[i-4])) + 
		     complex_mul(0.022, complex_mul(x[i], x[i-5])) +
		     complex_mul(0.009, complex_mul(x[i-1], x[i-3])) + 
		     complex_mul(0.019, complex_mul(x[i-3], complex_power(x[i-1], 2))) + 
		     complex_mul(0.01, complex_mul(x[i], complex_power(x[i-5], 3))) + 
		     complex_mul(0.05, complex_power(x[i], 2)) + 
		     complex_mul(0.02, complex_mul(x[i], x[i-2])) +
		     complex_mul(0.01, complex_power(x[i-1], 2)) + 
		     complex_mul(0.05, complex_power(x[i-2], 2));
      }
      // Tell runtime system how many output items we produced.
      return noutput_items;
    }


  } /* namespace ruiy */
} /* namespace gr */

