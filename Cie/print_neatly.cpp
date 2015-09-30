/**
 * You are given a sequence of words, and a limit on the number of characters
 * that can be put in one line (line width). You need to print the text neatly.
 * i.e. put line breaks in the given sequence of words such that the lines are
 * printed neatly. The condition is that the length of each word should be
 * smaller than the line width.
 *
 * The idea here is to have balanced lines. The extra spaces includes spaces put
 * at the end of every line except the last one. The problem is to minimize the
 * following total cost.
 *
 * Cost of a line = (Number of extra spaces in the line) ^ 3
 * Total cost = Sum of costs for all lines
 *
 * For example, consider the following string and line width M = 15.
 * "Geeks for Geeks presents word wrap problem"
 *
 * Following is the optimized arrangement of words in 3 lines:
 *
 * Geeks for Geeks|
 * presents word  |
 * wrap problem   |
 *
 * The total extra spaces in line 1, line 2 and line 3 are 0, 2 and 3
 * respectively. So optimal value of total cost is 0 + 2*2 + 3*3 = 13.
 */

#include "utils.h"
using namespace std;


int cal(vector<int> &nums, int k, int ind) {
  int n = nums.size();
  if (ind >= n) return 0;
  // if the nums from ind can be filled in a line, return it
  // k = 15 , fill 15/2 , 15/2 
  int tmpsum = nums[ind], halfsum = tmpsum, halfind = ind, i = ind;
  while (i < n - 1 && tmpsum < k) {
    tmpsum += nums[++i] + 1; // for space between words
    if (tmpsum >= k / 2 && halfsum < k / 2) {
      halfind = i;
      halfsum = tmpsum;
    }
  }
  // the length is less than k, return immediately
  if (i == n - 1 && tmpsum < k) return (k - tmpsum) * (k - tmpsum);

  // otherwise, recursively find the best
  // start point of the searching 
  // each line should have at least a length more than half of k
  //k =4, words=[a,aaaa]   a___ | aaaa 
  // k   words           |a a a           | 
  //                     |aaaaaaaaaaaaaa  |
  int tmpval = (k - halfsum) * (k - halfsum), minval = tmpval + cal(nums, k, halfind + 1);
  for (i = halfind + 1; i < n; ++i) {
    halfsum += nums[i] + 1;
    if (halfsum > k) break;
    tmpval = (k - halfsum) * (k - halfsum) + cal(nums, k, i + 1);
    if (tmpval < minval) minval = tmpval;
  }
  return minval;
}

int cal(vector<string> &strs, int k) {
  int n = strs.size();
  if (n == 0 || k == 0) return 0;
  vector<int> nums;
  for (int i = 0; i < n; ++i) nums.push_back(strs[i].length());
  return cal(nums, k, 0);
}

int main() {
    string ss[] = {"Geeks", "for", "Geeks", "presents", "word", "wrap", "problem"};
    string ss2[] = {"aaaaaaaaaa", "aaaa", "aaaaaaaa", "aaaaaaa", };// 10,4,8,7 k=15 -> 93
    vector<string> strs;
    int len = 7;
    int len2 = 4;
    for (int i = 0; i < len2; ++i) {
        strs.push_back(ss2[i]);
    }
    cout << cal(strs, 15) << endl;  
    return 0;
}