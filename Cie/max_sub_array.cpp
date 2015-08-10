// Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray is highlighted with blue rectangle and sum of this subarray is 29.

// http://www.geeksforgeeks.org/wp-content/uploads/rectangle.png

// This problem is mainly an extension of Largest Sum Contiguous Subarray for 1D array.

// time: from 9:20 to 9:46, no idea except for brute force or divide&conquer and brute force

// brute force
// btw, the answer of the image is not right, the largest sum shoud be the rectangle from (0,1) to (3,3)
#include "utils.h"
#define max(a,b)            (((a) > (b)) ? (a) : (b))
#define INT_MIN     (-2147483647 - 1) /* minimum (signed) int value */
int maxArr(vector<vector<int> > &mat) {
  int n = mat.size();
  if (n == 0) return 0;
  int m = mat[0].size();
  if (m == 0) return 0;
  vector<vector<int> > sum = mat;
  int res = INT_MIN;
  for (int i = 0; i < n; ++i) {
    for (int j = i; j < n; ++j) {
      if (i > 0) {
        // let sum[j] add mat[j]
        for (int l = 0; l < m; ++l) {
          // sum[j - 1] is the sum of mat[1 ~ j-1]
          // sum[j] = sum[j - 1] + mat[j]
          // o(n^3) 
          // o(logn * n^2)
          sum[j][l] = sum[j - 1][l] + mat[j][l];
        }
        // let sum[j] substract mat[j - i - 1] so that sum[j] is the rowsum of mat[j-i to j], i.e. sum of i+1 rows
        if (j > i) {
          for (int l = 0; l < m; ++l) {
            sum[j][l] -= mat[j - i - 1][l];
          }
        }
      }
      // sum[j] is a row, and the code below is to find the maxsumsubarr of sum[j]
      int tmpsum = 0;
      for (int k = 0; k < m; ++k) {
        if (tmpsum < 0) tmpsum = 0;
        if (tmpsum + sum[j][k] > 0) { tmpsum += sum[j][k]; }
        else { tmpsum = sum[j][k]; }
        res = max(res, tmpsum);
      }
    }
  }
  return res;
}

int main() {
    vector<vector<int> > mat1;
    vector<int> r1;
    r1.push_back(1);
    r1.push_back(2);
    r1.push_back(-1);
    r1.push_back(4);
    r1.push_back(-20);
    vector<int> r2;
    r2.push_back(-8);
    r2.push_back(-3);
    r2.push_back(4);
    r2.push_back(2);
    r2.push_back(1);
    vector<int> r3;
    r3.push_back(3);
    r3.push_back(8);
    r3.push_back(10);
    r3.push_back(-8);
    r3.push_back(3);
    vector<int> r4;
    r4.push_back(-4);
    r4.push_back(-1);
    r4.push_back(1);
    r4.push_back(7);
    r4.push_back(-6);
    mat1.push_back(r1);
    mat1.push_back(r2);
    mat1.push_back(r3);
    mat1.push_back(r4);
    
    cout << maxArr(mat1) << endl;
    return 0;
}