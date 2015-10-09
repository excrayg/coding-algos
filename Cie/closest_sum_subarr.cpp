// problem2: find closest sub array sum. 
// given an array and a target number, return the sum of sub array that closest to the target


// find closest sum of subset of an array to a target
// [-1, 4, 9] target = 8, return 8 = -1 + 9

// [x, x, x, x, x] 

#include "utils.h"

int closest(vector<int> &nums, int target) {
    int n = nums.size();
    if (n == 0) return 0;
    if (n == 1) return nums[0];
    
    int res = nums[0], start = 0, end = 0;
    sort(nums.begin(), nums.end());
    while (end < n) {
        if (res == target) return target;
        while (res < target) res += 
    }
    
    
}