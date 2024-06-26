###################################################################################
##                                            __ _      _     _                  ##
##                                           / _(_)    | |   | |                 ##
##                __ _ _   _  ___  ___ _ __ | |_ _  ___| | __| |                 ##
##               / _` | | | |/ _ \/ _ \ '_ \|  _| |/ _ \ |/ _` |                 ##
##              | (_| | |_| |  __/  __/ | | | | | |  __/ | (_| |                 ##
##               \__, |\__,_|\___|\___|_| |_|_| |_|\___|_|\__,_|                 ##
##                  | |                                                          ##
##                  |_|                                                          ##
##                                                                               ##
##                                                                               ##
##              Peripheral-NTM for MPSoC                                         ##
##              Neural Turing Machine for MPSoC                                  ##
##                                                                               ##
###################################################################################

###################################################################################
##                                                                               ##
## Copyright (c) 2022-2023 by the author(s)                                      ##
##                                                                               ##
## Permission is hereby granted, free of charge, to any person obtaining a copy  ##
## of this software and associated documentation files (the "Software"), to deal ##
## in the Software without restriction, including without limitation the rights  ##
## to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     ##
## copies of the Software, and to permit persons to whom the Software is         ##
## furnished to do so, subject to the following conditions:                      ##
##                                                                               ##
## The above copyright notice and this permission notice shall be included in    ##
## all copies or substantial portions of the Software.                           ##
##                                                                               ##
## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    ##
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      ##
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   ##
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        ##
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, ##
## OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN     ##
## THE SOFTWARE.                                                                 ##
##                                                                               ##
## ============================================================================= ##
## Author(s):                                                                    ##
##   Paco Reina Campo <pacoreinacampo@queenfield.tech>                           ##
##                                                                               ##
###################################################################################

import numpy as np

from tensor.adder import ntm_tensor_adder as tensor_adder
from tensor.subtractor import ntm_tensor_subtractor as tensor_subtractor
from tensor.multiplier import ntm_tensor_multiplier as tensor_multiplier
from tensor.divider import ntm_tensor_divider as tensor_divider

def test_tensor_adder():

  data_a_in = np.random.rand(3,3,3)
  data_b_in = np.random.rand(3,3,3)

  np.testing.assert_array_equal(tensor_adder.ntm_tensor_adder(data_a_in, data_b_in), data_a_in + data_b_in)

def test_tensor_subtractor():

  data_a_in = np.random.rand(3,3,3)
  data_b_in = np.random.rand(3,3,3)

  np.testing.assert_array_equal(tensor_subtractor.ntm_tensor_subtractor(data_a_in, data_b_in), data_a_in - data_b_in)

def test_tensor_multiplier():

  data_a_in = np.random.rand(3,3,3)
  data_b_in = np.random.rand(3,3,3)

  np.testing.assert_array_equal(tensor_multiplier.ntm_tensor_multiplier(data_a_in, data_b_in), data_a_in * data_b_in)

def test_tensor_divider():

  data_a_in = np.random.rand(3,3,3)
  data_b_in = np.random.rand(3,3,3)

  np.testing.assert_array_equal(tensor_divider.ntm_tensor_divider(data_a_in, data_b_in), data_a_in / data_b_in)


test_tensor_adder()
test_tensor_subtractor()
test_tensor_multiplier()
test_tensor_divider()
