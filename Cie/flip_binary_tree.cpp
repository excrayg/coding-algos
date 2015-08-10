// Given a binary tree where all the right nodes are either leaf nodes with a sibling (a left node that shares the same parent node) or empty, flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes . Return the new root.
 
// For Example:
// Given a binary Tree {1,2,3,4,5},
//    1
//  /  \
//  2   3
// / \
// 4 5
 
// return the root of the binary Tree [4,5,2, #, #, 3,1].
// 4
// / \
// 5 2
//   / \
//  3    1