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
## Copyright (c) 2020-2024 by the author(s)                                      ##
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

def dnc_trained_top(X_IN):
  # Constants
  LENGTH_IN = 3

  SIZE_T_IN = 3
  SIZE_X_IN = 3
  SIZE_Y_IN = 3
  SIZE_N_IN = 3
  SIZE_W_IN = 3
  SIZE_L_IN = 3
  SIZE_R_IN = 3

  SIZE_S_IN = 3*SIZE_W_IN + 3
  SIZE_M_IN = SIZE_W_IN + 5

  # Signals
  P_IN = np.rand(SIZE_R_IN, SIZE_Y_IN, SIZE_W_IN)
  Q_IN = np.rand(SIZE_Y_IN, SIZE_L_IN)

  w_int = np.rand(SIZE_L_IN, SIZE_X_IN)
  k_int = np.rand(SIZE_R_IN, SIZE_L_IN, SIZE_X_IN)
  v_int = np.rand(SIZE_L_IN, SIZE_S_IN)
  d_int = np.rand(SIZE_R_IN, SIZE_L_IN, SIZE_M_IN)
  u_int = np.rand(SIZE_L_IN, SIZE_L_IN)
  b_int = np.rand(SIZE_L_IN, 1)

  # Body
  Y_OUT, R_OUT, XI_OUT, RHO_OUT, H_OUT = dnc_interface_top(w_int, k_int, v_int, d_int, u_int, b_int, P_IN, Q_IN, X_IN)

  w_int, k_int, v_int, d_int, u_int, b_int = ntm_fnn_trainer(X_IN, R_OUT, XI_OUT, RHO_OUT, H_OUT, LENGTH_IN)

  Y_OUT, R_OUT, XI_OUT, RHO_OUT, H_OUT = dnc_interface_top(w_int, k_int, v_int, d_int, u_int, b_int, P_IN, Q_IN, X_IN)

  return Y_OUT, R_OUT, XI_OUT, RHO_OUT, H_OUT
