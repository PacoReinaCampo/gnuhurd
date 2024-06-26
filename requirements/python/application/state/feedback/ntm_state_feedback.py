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

def ntm_state_matrix_feedforward(data_k_in, data_d_in):
  # Package

  # Constants
  # SIZE: A[N,N]; B[N,P]; C[Q,N]; D[Q,P];
  # SIZE: K[P,P]; x[N,1]; y[Q,1]; u[P,1];

  SIZE_D_I_IN, SIZE_D_J_IN = data_d_in.shape

  ntm_matrix_eye = np.eye(SIZE_D_I_IN)

  # Body
  # d = inv(I + D·K)·D
  matrix_operation_int = ntm_matrix_product(data_d_in, data_k_in)

  matrix_operation_int = ntm_matrix_adder(ntm_matrix_eye, matrix_operation_int)

  matrix_operation_int = ntm_matrix_inverse(matrix_operation_int)

  data_d_out = ntm_matrix_product(matrix_operation_int, data_d_in)

  return data_d_out

def ntm_state_matrix_input(data_k_in, data_b_in, data_d_in):
  # Package

  # Constants
  # SIZE: A[N,N]; B[N,P]; C[Q,N]; D[Q,P];
  # SIZE: K[P,P]; x[N,1]; y[Q,1]; u[P,1];

  SIZE_D_I_IN, SIZE_D_J_IN = data_d_in.shape

  ntm_matrix_eye = np.eye(SIZE_D_I_IN)

  # Body
  # b = B·(I-K·inv(I + D·K)·D)
  matrix_operation_int = ntm_matrix_product(data_d_in, data_k_in)

  matrix_operation_int = ntm_matrix_adder(ntm_matrix_eye, matrix_operation_int)

  matrix_operation_int = ntm_matrix_inverse(matrix_operation_int)

  matrix_operation_int = ntm_matrix_product(matrix_operation_int, data_d_in)

  matrix_operation_int = ntm_matrix_product(data_k_in, matrix_operation_int)

  matrix_operation_int = ntm_matrix_substractor(ntm_matrix_eye, matrix_operation_int)

  data_b_out = ntm_matrix_product(data_b_in, matrix_operation_int)

  return data_b_out

def ntm_state_matrix_output(data_k_in, data_c_in, data_d_in):
  # Package

  # Constants
  # SIZE: A[N,N]; B[N,P]; C[Q,N]; D[Q,P];
  # SIZE: K[P,P]; x[N,1]; y[Q,1]; u[P,1];

  SIZE_D_I_IN, SIZE_D_J_IN = data_d_in.shape

  ntm_matrix_eye = np.eye(SIZE_D_I_IN)

  # Body
  # c = inv(I + D·K)·C
  matrix_operation_int = ntm_matrix_product(data_d_in, data_k_in)

  matrix_operation_int = ntm_matrix_adder(ntm_matrix_eye, matrix_operation_int)

  matrix_operation_int = ntm_matrix_inverse(matrix_operation_int)

  data_c_out = ntm_matrix_product(matrix_operation_int, data_c_in)

  return data_c_out

def ntm_state_matrix_state(data_k_in, data_a_in, data_b_in, data_c_in, data_d_in):
  # Package

  # Constants
  # SIZE: A[N,N]; B[N,P]; C[Q,N]; D[Q,P];
  # SIZE: K[P,P]; x[N,1]; y[Q,1]; u[P,1];

  SIZE_D_I_IN, SIZE_D_J_IN = data_d_in.shape

  ntm_matrix_eye = np.eye(SIZE_D_I_IN)

  # Body
  # a = A-B·K·inv(I + D·K)·C
  matrix_operation_int = ntm_matrix_product(data_d_in, data_k_in)

  matrix_operation_int = ntm_matrix_adder(ntm_matrix_eye, matrix_operation_int)

  matrix_operation_int = ntm_matrix_inverse(matrix_operation_int)

  matrix_operation_int = ntm_matrix_product(matrix_operation_int, data_c_in)

  matrix_operation_int = ntm_matrix_product(data_k_in, matrix_operation_int)

  matrix_operation_int = ntm_matrix_product(data_b_in, matrix_operation_int)

  data_a_out = ntm_matrix_adder(data_a_in, matrix_operation_int)

  return data_a_out
