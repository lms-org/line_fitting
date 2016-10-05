//
// Academic License - for use in teaching, academic research, and meeting
// course requirements at degree granting institutions only.  Not for
// government, commercial, or other organizational use.
// File: xscal.cpp
//
// MATLAB Coder version            : 3.0
// C/C++ source code generated on  : 29-Nov-2015 11:30:09
//

// Include Files
#include "rt_nonfinite.h"
#include "kalman_filter_lr.h"
#include "xscal.h"

// Function Definitions

//
// Arguments    : int n
//                double a
//                emxArray_real_T *x
//                int ix0
// Return Type  : void
//
void xscal(int n, double a, emxArray_real_T *x, int ix0)
{
  int i11;
  int k;
  i11 = (ix0 + n) - 1;
  for (k = ix0; k <= i11; k++) {
    x->data[k - 1] *= a;
  }
}

//
// File trailer for xscal.cpp
//
// [EOF]
//
