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


#ifndef INCLUDED_RUIY_CARRIER_OFFSET_H
#define INCLUDED_RUIY_CARRIER_OFFSET_H

#include <ruiy/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace ruiy {

    /*!
     * \brief <+description of block+>
     * \ingroup ruiy
     *
     */
    class RUIY_API carrier_offset : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<carrier_offset> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of ruiy::carrier_offset.
       *
       * To avoid accidental use of raw pointers, ruiy::carrier_offset's
       * constructor is in a private implementation
       * class. ruiy::carrier_offset::make is the public interface for
       * creating new instances.
       */
      static sptr make(float df_f0_ratio);
    };

  } // namespace ruiy
} // namespace gr

#endif /* INCLUDED_RUIY_CARRIER_OFFSET_H */

