// Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

// Examples

// arr[] = {1, 5, 11, 5}
// Output: true 
// The array can be partitioned as {1, 5, 5} and {11}

// arr[] = {1, 5, 3}
// Output: false 
// The array cannot be partitioned into equal sum sets.

// time: from 9:06 to 9:40

#include "utils.h"
#include <algorithm>

// check if exists numbers in nums[0 to ind] sum to sum.
bool hasSum(const vector<int> &nums, int ind, int sum) {
    if (sum == 0) return true;
    if (ind < 0 || sum < 0) return false;
    return hasSum(nums, ind - 1, sum - nums[ind]) || hasSum(nums, ind - 1, sum);
}

bool partitionable(vector<int> &nums) {
    int n = nums.size();
    if (n == 0) return true;
    if (n == 1) return false;
    int sum = 0;
    for (int i = 0; i < n; ++i) sum += nums[i];
    if (sum & 1) return false; // if sum is odd, return false
    sort(nums.begin(), nums.end());
    sum /= 2; // sum of one set
    sum -= nums[n - 1]; // sum of the set that contains the largest number
    return hasSum(nums, n - 2, sum);    
}

int main() {
    vector<int> tst1;
    tst1.push_back(1);
    tst1.push_back(5);
    tst1.push_back(3);
    vector<int> tst2;
    tst2.push_back(11);
    tst2.push_back(5);
    tst2.push_back(5);
    tst2.push_back(1);
    vector<int> tst3;
    tst3.push_back(11);
    tst3.push_back(2);
    tst3.push_back(3);
    tst3.push_back(1);
    tst3.push_back(7);
    cout << partitionable(tst1) << endl;
    cout << partitionable(tst2) << endl;
    cout << partitionable(tst3) << endl;
    return 0;
}