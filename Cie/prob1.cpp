// Follow up for "Search in Rotated Sorted Array":
// What if duplicates are allowed?

// Would this affect the run-time complexity? How and why?

// Write a function to determine if a given target is in the array.


// with duplicates

int search(const vector<int> &nums, int start, int end, int k) {
    if (start > end) return -1;
    int mid;
    while (start <= end) {
        mid = start + (end - start) / 2;
        if (nums[mid] == k) return mid;
        //every start:end 
        //nums[mid] == nums[start] && nums[mid] == nums[end])
        //means num[start] == num[end] ? 33333312333
        if (nums[mid] == nums[start] && nums[mid] == nums[end]) {
            int tmp = search(nums, start, mid - 1, k);
            if (tmp >= 0) return tmp;
            tmp = search(nums, mid + 1, end, k);
            if (tmp >= 0) return tmp;
            return -1;
        }
        // if k < num[mid], end = mid - 1 if array is not rotated
        // if array is rotated : 
        // 
        if (nums[mid] > k) {
            // below condition: the rotate position is between start and mid
            // if (nums[start] <= k ) k is between start and mid
            
            if (nums[start] <= k || nums[start] > nums[mid]) {
                end = mid - 1;
            } else {
                start = mid + 1; // -- but k < nums[mid] right? so when does this happen 4567123 1
                //rotate point is in mid:end
            }
        } else { //same thing in reverse
            if (nums[end] >= k || nums[end] < nums[mid]) {
                start = mid + 1;
            } else {
                end = mid - 1;
            }
        }
    }
    return -1;
}

int search(const vector<int> &nums, int k) {
    int n = nums.size();
    if (n == 0) return false;
    int res = search(nums, 0, n - 1, k);
    return res;
}