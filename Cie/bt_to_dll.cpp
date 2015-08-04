// Given a Binary Tree (Bt), convert it to a Doubly Linked List(DLL). The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.

// Input: 
//   10
//   /  \ 
//  2    13
//      /
//     11
    
// Output:
// 2 <-> 10 <-> 11 <-> 13

//Time taken: from:8:46 to:9:09
#include <iostream>
#include "utils.h"
using namespace std;



ListNode* btTodll(TreeNode *root) {
    if (!root) return NULL;
    ListNode *linkroot = new ListNode(0);
    ListNode *lp = linkroot;
    TreeNode *p = root, *tmp;
    while (p) {
        if (!p->left) { // meet a left leaf node
            // handle p
            ListNode *ltmp = new ListNode(p->val);
            lp->next = ltmp;
            ltmp->pre = lp;
            lp = ltmp;
            p = p->right;
            continue;
        } 
        
        tmp = p->left;
        while (tmp->right && tmp->right != p) { // find the pre node of in-order traverse
            tmp = tmp->right;
        }
        if (tmp->right == NULL) { // if the pre node's right is NULL, set the pre node's right to p
            tmp->right = p;
            p = p->left;
        } else { // if the pre node's right is already set to p, then we should handle p now
            // first reset the pre node's right to NULL
            tmp->right = NULL;
            // handle p
            ListNode *ltmp = new ListNode(p->val);
            lp->next = ltmp;
            ltmp->pre = lp;
            lp = ltmp;
            p = p->right;
        }
    }
    linkroot->next->pre = NULL;
    return linkroot->next;
}

int main() {
    TreeNode *t1 = new TreeNode(1);
    TreeNode *t2 = new TreeNode(2);
    TreeNode *t3 = new TreeNode(3);
    TreeNode *t4 = new TreeNode(4);
    t2->left = t1;
    t2->right = t4;
    t4->left = t3;
    ListNode *res = btTodll(t2);
    
    while (res) {
        cout << res->val << endl;
        res = res->next;
    }
    
    return 0;
}