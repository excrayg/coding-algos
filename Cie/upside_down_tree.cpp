// Given a binary tree where all the right nodes are either leaf nodes with a sibling 
// (a left node that shares the same parent node) or empty, 
// flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes . 
// Return the new root.
 
// For Example:
// Given a binary Tree {1,2,3,4,5},
//    1
//   / \
//  2   3
// / \
// 4 5
 
// return the root of the binary Tree [4,5,2, #, #, 3,1].
// 4
// / \
// 5 2
//   / \
// 3    1

#include "utils.h"

void print(TreeNode *root) {
    queue<TreeNode*> q;
    q.push(root);
    cout << root->val << ",";
    while (!q.empty()) {
        root = q.front();
        q.pop();
        if (root->left) {cout << root->left->val << ","; q.push(root->left);}
        else cout << "#,";
        if (root->right) { cout << root->right->val << ","; q.push(root->right); }
        else cout << "#,";
    }
}

TreeNode* flip(TreeNode *root) {
    stack<TreeNode*> st;
    if (!root || !root->left) return root;
    TreeNode *p = root;
    while (p->left) {
        st.push(p);
        p = p->left;
    }
    root = p;
    while (!st.empty()) {
        p->left = st.top()->right;
        p->right = st.top();
        p = st.top();
        p->left = NULL;
        p->right = NULL;
        st.pop();
    }
    p->right = NULL;
    return root;
}

int main() {
    TreeNode *t1 = new TreeNode(1);
    TreeNode *t2 = new TreeNode(2);
    TreeNode *t3 = new TreeNode(3);
    TreeNode *t4 = new TreeNode(4);
    TreeNode *t5 = new TreeNode(5);
    TreeNode *t6 = new TreeNode(6);
    t1->left = t2;
    t1->right = t3;
    t2->left = t4;
    t2->right = t5;
    TreeNode *res = flip(t1);
    print(res);
    return 0;
}