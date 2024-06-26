///////////////////////////////////////////////////////////////////////////////////
//                                            __ _      _     _                  //
//                                           / _(_)    | |   | |                 //
//                __ _ _   _  ___  ___ _ __ | |_ _  ___| | __| |                 //
//               / _` | | | |/ _ \/ _ \ '_ \|  _| |/ _ \ |/ _` |                 //
//              | (_| | |_| |  __/  __/ | | | | | |  __/ | (_| |                 //
//               \__, |\__,_|\___|\___|_| |_|_| |_|\___|_|\__,_|                 //
//                  | |                                                          //
//                  |_|                                                          //
//                                                                               //
//                                                                               //
//              Peripheral-NTM for MPSoC                                         //
//              Neural Turing Machine for MPSoC                                  //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////////
//                                                                               //
// Copyright (c) 2020-2024 by the author(s)                                      //
//                                                                               //
// Permission is hereby granted, free of charge, to any person obtaining a copy  //
// of this software and associated documentation files (the "Software"), to deal //
// in the Software without restriction, including without limitation the rights  //
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell     //
// copies of the Software, and to permit persons to whom the Software is         //
// furnished to do so, subject to the following conditions:                      //
//                                                                               //
// The above copyright notice and this permission notice shall be included in    //
// all copies or substantial portions of the Software.                           //
//                                                                               //
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR    //
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,      //
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE   //
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER        //
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, //
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN     //
// THE SOFTWARE.                                                                 //
//                                                                               //
// ============================================================================= //
// Author(s):                                                                    //
//   Paco Reina Campo <pacoreinacampo@queenfield.tech>                           //
//                                                                               //
///////////////////////////////////////////////////////////////////////////////////

pub struct ScalarMath {
    pub data_in: Vec<Vec<f64>>,
    pub mean_in: Vec<f64>,

    pub Vec<f64>
}

impl ScalarMath {
    pub fn ntm_vector_deviation_function(data_in: Vec<Vec<f64>>, mean_in: Vec<f64>) -> Vec<f64> {
        let mut data_out: Vec<f64> = vec![];

        for i in 0..data_in.len() {
            let mut temporal: f64 = 0.0;

            for j in 0..data_in[i].len() {
                temporal += (data_in[i][j] - mean_in[i])*(data_in[i][j] - mean_in[i])/data_in[0].len() as f64;
            }
            data_out.push(temporal.sqrt());
        }
        data_out
    }
    pub fn ntm_vector_logistic_function(data_in: Vec<f64>) -> Vec<f64> {

        const ONE: f64 = 1.0;

        let mut data_out: Vec<f64> = vec![];

        for i in 0..data_in.len() {
            let temporal = ONE/(ONE + ONE/data_in[i].exp());

            data_out.push(temporal);
        }
        data_out
    }
    pub fn ntm_vector_mean_function(data_in: Vec<Vec<f64>>) -> Vec<f64> {
        let mut data_out: Vec<f64> = vec![];

        for i in 0..data_in.len() {
            let mut temporal: f64 = 0.0;

            for j in 0..data_in[i].len() {
                temporal += data_in[i][j]/data_in[0].len() as f64;
            }
            data_out.push(temporal);
        }
        data_out
    }
    pub fn ntm_vector_oneplus_function(data_in: Vec<f64>) -> Vec<f64> {

        const ONE: f64 = 1.0;

        let mut data_out: Vec<f64> = vec![];

        for i in 0..data_in.len() {
            let temporal0: f64 = ONE + data_in[i].exp();
            let temporal1: f64 = ONE + temporal0.ln();

            data_out.push(temporal1);
        }
        data_out
    }
}
