 //Given an array a contains all digits 0-9 a   = [1, 4, 2, 1] # which represents 1421 Add one to the number and return the array return a = [1, 4, 2, 2] # which represents 1422 . Identify all corner cases. 

// cases: 0, 1, 9, 10, 11, 19, 29, 99, 999, 999999999, 1999999999, 
// time: from 11:19 to 11:33

//Correct 

#include <iostream>
#include <vector>
using namespace std;

void addOne(vector<int> &num) {
    int n = num.size();
    if (n == 0) {
        num.push_back(1);
        return;
    } 
    --n;
    while (n >= 0) {
        if (num[n] < 9) {
            ++num[n];
            return;
        }
        num[n] = 0;
        --n;
    }
    num.insert(num.begin(), 1);
}

template <class T>
void print(const vector<T> &v) {
    int n = v.size();
    
    for (int i = 0; i < n; ++i) {
        cout << v[i] << "\t";
    }
    cout << endl;
}

int main() {
    vector<int> num1(1, 1);
    vector<int> num2(1, 9);
    vector<int> num3(1, 1);
    num3.push_back(9);
    num3.push_back(9);
    num3.push_back(9);
    addOne(num1);
    addOne(num2);
    addOne(num3);
    print(num1);
    print(num2);
    print(num3);
    return 0;
}