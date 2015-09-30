/*
compute the maximum subarray sum in circular array
Given a circular array A, compute it maximum subarray sum in O(n) time. Can you devise it in
O(1) space too. 

*/


// [a, b, c, ... x]  maxsubarr of 0~n-1
// [a, b, c, ..k, x] maxsubarr of k~n-1,0,..k-1
// [-1, -2] -1

// [4, -1, 4, -5, 1]


#include "utils.h"
using namespace std;
int maxSub(vector<int> &nums, int start) {
    int n = nums.size();
    if (n == 0 || start >= n ) return 0;
    int res = nums[start], tmpsum = res;
    if (n == 1) return res;
    for (int i = start + 1; i != start; ++i, i %= n) {
        if (tmpsum < 0) tmpsum = 0;
        tmpsum += nums[i];
        if (tmpsum > res) res = tmpsum;
    }
    return res;
}

int maxSub(vector<int> &nums) {
    int n = nums.size();
    if (n == 0) return 0;
    int ind = n, tmpsum = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] < 0) { ind = i; break; }
    }
    if (ind == n)  return maxSub(nums, 0);
    return max(maxSub(nums, 0), maxSub(nums, ind));
}

int secondMaxSub(vector<int> &nums) {
    int n = nums.size();
    if (n == 0) return 0;
    int res = nums[0], tmpsum = res, start = 0;
    if (n == 1) return res;
    for (int i = 1; start < n; ++i, i %= n) {
        if (i == start) break;
        if (tmpsum <= 0) { 
            tmpsum = 0;
            if (start > i) break;
            start = i; 
        }
        tmpsum += nums[i];
        if (tmpsum > res) res = tmpsum;
    }
    return res;
}

int main() {
    vector<int> nums;
    nums.push_back(-2);
    nums.push_back(-1);
    
    vector<int> nums2;
    nums2.push_back(-2);
    nums2.push_back(1);
    nums2.push_back(1);
    
    vector<int> nums3;
    nums3.push_back(2);
    nums3.push_back(-1);
    nums3.push_back(1);
    
    vector<int> nums4;
    nums4.push_back(4);
    nums4.push_back(-1);
    nums4.push_back(4);
    nums4.push_back(-5);
    nums4.push_back(3);
    nums4.push_back(-5);
    nums4.push_back(2);
    nums4.push_back(-1);
    nums4.push_back(1);
    
    vector<int> nums5;
    nums5.push_back(0);
    nums5.push_back(0);
    nums5.push_back(0);
    
    cout << maxSub(nums) << endl;
    cout << maxSub(nums2) << endl;
    cout << maxSub(nums3) << endl;
    cout << maxSub(nums4) << endl;
    cout << maxSub(nums5) << endl;
    
    cout << secondMaxSub(nums) << endl;
    cout << secondMaxSub(nums2) << endl;
    cout << secondMaxSub(nums3) << endl;
    cout << secondMaxSub(nums4) << endl;
    cout << secondMaxSub(nums5) << endl;
    return 0;
}