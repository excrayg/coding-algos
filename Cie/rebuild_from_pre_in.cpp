// problem1: rebuild a bt from its preorder and inorder traverse

#include "utils.h"
using namespace std;

bool has_error = false;
TreeNode* rebuild(string pre, string in) {
    if (pre.length() == 0 || in.length() == 0) {
        if (pre.length() > 0 || in.length() > 0) has_error = true;
        return NULL;
    }
    TreeNode *root = new TreeNode(pre[0] - '0');
    int ind = 0;
    for (int i = 0; i < in.length(); ++i) {
        if (in[i] == pre[0]) {
            ind = i;
            break;
        }
    }
    if (i == in.length()) {
        has_error = true;
        return NULL;
    }
    root->left = rebuild(pre.substr(1, ind), in.substr(0, ind));
    root->right = rebuild(pre.substr(ind + 1), in.substr(ind + 1));
    return root;
}

void print(TreeNode* root) {
    if (!root) { cout << "#,"; return; }
    cout << root->val << ",";
    print(root->left);
    print(root->right);
}

int main() {
    //   _1_  
    //  2  _4   => 1243, 2134
    //    3
    //   _1
    // _2      => 123, 321
    //3
    //   1_
    //     2_  => 123, 123
    //       3
    
    TreeNode* res1 = rebuild("1243", "2134");
    TreeNode* res2 = rebuild("123", "321");
    TreeNode* res3 = rebuild("123", "123");
    print(res1);
    cout << endl;
    print (res2);
    cout << endl;
    print (res3);
    cout << endl;
    return 0;
}