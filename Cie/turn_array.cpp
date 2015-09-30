

#include "utils.h"

void swap(int &a, int &b) {
    a = a^b;
    b = a^b;
    a = a^b;
}

// [1,2,3,4,5,6]
// [1,2,4,5,3,6]
// [1,2,4,5,     3,6]
// [1,4,  2,5,   3,6]
void turn(vector<int> &arr, int start, int end) {
    if (start >= end - 1) return;
    int half = (end + 1 - start) / 2;
    int s = start, e = end, m = s + half / 2;
    half = (half + 1) / 2;
    for (int i = 0; i < half; ++i) {
        swap(arr[m + i], arr[m + half + i]);
    }
    print(arr);
    turn(arr, start, m + half);
    turn(arr, m + half + 1, end);
}

void turn(vector<int> &arr) {
    int n = arr.size();
    if (n < 3) return;
    turn(arr, 0, n - 1);
    print(arr);
}

int main() {
    vector<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(3);
    arr.push_back(4);
    arr.push_back(5);
    arr.push_back(6);
    turn(arr);
    
    return 0;
}