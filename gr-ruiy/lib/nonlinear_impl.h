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

#ifndef INCLUDED_RUIY_NONLINEAR_IMPL_H
#define INCLUDED_RUIY_NONLINEAR_IMPL_H

#include <ruiy/nonlinear.h>

namespace gr {
  namespace ruiy {

    class nonlinear_impl : public nonlinear
    {
     private:
      // Nothing to declare in this block.

	  bool d_is_nonlinear;
     public:
      nonlinear_impl(bool is_nonlinear);
      ~nonlinear_impl();

      // Where all the action really happens
      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

	  gr_complex complex_power(gr_complex b, int num);
	  gr_complex complex_mul(gr_complex a, gr_complex b);
      int general_work(int noutput_items,
           gr_vector_int &ninput_items,
           gr_vector_const_void_star &input_items,
           gr_vector_void_star &output_items);
    };

  } // namespace ruiy
} // namespace gr

#endif /* INCLUDED_RUIY_NONLINEAR_IMPL_H */

