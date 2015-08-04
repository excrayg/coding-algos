//  Compute the successor. The successor of a node n in a binary tree is the node s that appears immediately after n in an inorder traversal. 
//  Design an algorithm that takes a node n in a binary tree, and returns its successor. Assume that each node has a parent field; the parent field of root is null.

// time: from 10:58 to 11:17

#include <iostream>
#include "utils.h"
using namespace std;

ParrentTreeNode* getSuccessor(ParrentTreeNode *nd) {
    if (!nd) return NULL;
    ParrentTreeNode *res = NULL;
    if (nd->right) {
        res = nd->right;
        while (res->left) res = res->left;    //Correct
        return res;
    }
    res = nd->parent;
    while (res && res->right == nd) {
        nd = res;
        res = res->parent;  //Correct
    }
    return res;
}

int main() {
    ParrentTreeNode *pt1 = new ParrentTreeNode(1);
    ParrentTreeNode *pt2 = new ParrentTreeNode(2);
    ParrentTreeNode *pt3 = new ParrentTreeNode(3);
    ParrentTreeNode *pt4 = new ParrentTreeNode(4);
    //  /1\
    //2\   3
    //  4 
    // result: 3, 4, NULL, 1
    
    pt1->left = pt2;
    pt2->parent = pt1;
    pt1->right = pt3;
    pt3->parent = pt1;
    pt2->right = pt4;
    pt4->parent = pt2;
    ParrentTreeNode *tmp = NULL;
    tmp = getSuccessor(pt1);
    if (tmp) cout << tmp->val << endl;
    else cout << "NULL" << endl;
    tmp = getSuccessor(pt2);
    if (tmp) cout << tmp->val << endl;
    else cout << "NULL" << endl;
    tmp = getSuccessor(pt3);
    if (tmp) cout << tmp->val << endl;
    else cout << "NULL" << endl;
    tmp = getSuccessor(pt4);
    if (tmp) cout << tmp->val << endl;
    else cout << "NULL" << endl;
    return 0;
}