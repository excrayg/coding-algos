#ifndef CIE_UTILS_H_
#define CIE_UTILS_H_
#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include "string"
using std::string;
using std::cout;
using std::endl;
using std::vector;
using std::stack;
using std::queue;
class TreeNode {
    public:
    int val;
    TreeNode *left, *right;
    TreeNode(int v) : val(v), left(NULL), right(NULL) {}
};

class ListNode {
    public:
    int val;
    ListNode *pre, *next;
    ListNode(int v) : val(v), pre(NULL), next(NULL) {}
};

class ParrentTreeNode {
    public:
    int val;
    ParrentTreeNode *left, *right, *parent;
    ParrentTreeNode(int v) : val(v), left(NULL), right(NULL), parent(NULL) {}
};

template <class T>
void print(const vector<T> &v) {
    int n = v.size();
    
    for (int i = 0; i < n; ++i) {
        cout << v[i] << "\t";
    }
    cout << endl;
}

#endif