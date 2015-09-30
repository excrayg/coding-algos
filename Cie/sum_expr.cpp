// . Suppose you are given a sequence of integers separated by + and − signs; for example:
// 1 + 3 − 2 − 5 + 1 − 6 + 7
// You can change the value of this expression by adding parentheses in different places. For
// example:
// 1 + 3 − 2 − 5 + 1 − 6 + 7 = −1
// (1 + 3 − (2 − 5)) + (1 − 6) + 7 = 9
// (1 + (3 − 2)) − (5 + 1) − (6 + 7) = −17
// Describe and analyze an algorithm to compute, given a list of integers separated by + and
// − signs, the maximum possible value the expression can take by adding parentheses.
// You may only use parentheses to group additions and subtractions; in particular, you
// are not allowed to create implicit multiplication as in 1 + 3(−2)(−5) + 1 − 6 + 7 = 33.




// presume there's no negative sign like 1 - -2

int calMin(vector<int> &nums, int ind_num, int end_num, vector<char> &ops, int ind_op) {
    if (ind_num == end_num) return nums[ind_num];
    int res = nums[ind_num++];
    while (ind_num <= end_num && ops[ind_op] == '+') {
        res += nums[ind_num++];
        ++ind_op;
    }
    if (ind_num > end_num) return res;
    int tmp;
    for (int i = 1; i <= end_num - ind_num; ++i) {
        if (ops[ind_op + i] == '-') {
            while (i <= end_num - ind_num && ops[ind_op] == '-') ++i;
            --i;
            tmp = res - calMax(nums, ind_num, ind_num + i, ops, ind_op);
            if (i < end_num - ind_num) tmp += calMin(nums, ind_num + i + 1, end_num, ops, ind_op + i + 1);
            if (tmp < res) res = tmp;
        }
    }
    return res;
}

int calMax(vector<int> &nums, int ind_num, int end_num, vector<char> &ops, int ind_op) {
    if (ind_num == end_num) return nums[ind_num];
    int res = nums[ind_num++];
    while (ind_num <= end_num && ops[ind_op] == '+') {
        res += nums[ind_num++];
        ++ind_op;
    }
    if (ind_num > end_num) return res;
    int tmp;
    for (int i = 1; i <= end_num - ind_num; ++i) {
        if (ops[ind_op + i] == '-') {
            while (i <= end_num - ind_num && ops[ind_op] == '-') ++i;
            --i;
            tmp = res - calMin(nums, ind_num, ind_num + i, ops, ind_op);
            if (i < end_num - ind_num) tmp += calMax(nums, ind_num + i + 1, end_num, ops, ind_op + i + 1);
            if (tmp > res) res = tmp;
        }
    }
    return res;
}

int cal(string s) {
    // TODO: validation of s
    stringstream ss(s);
    int num;
    char c;
    vector<int> nums;
}