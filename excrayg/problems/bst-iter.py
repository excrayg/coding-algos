
#Problem: implement an external iterator for a Binary Search Tree which provides two APIs: hasNext(), next().
#Notice next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree

#inorder traversal

#Starttime1 : 3:10 pm
#endtime1:  3:35 pm

#First Attempt - Incorrect.
		

#Attempt 2 - Correct	
#starttime2 8:15 PM
#endtime2 8:30 PM
import sys
class BST:
	
	def __init__(self, root):
		#root assumed to be non-null
		self.node = root
		self.stack = []
		self.stack.append(root)
		
	def hasNext(self):
		if len(self.stack) > 0:
			return True
		return False
		
	#No idea how to make it O(1)
	#Maybe since n/2 nodes are leaf nodes, maybe this averages to O(1)
	#The stack grows to height of the tree. This is basically an iterator over inorder traversal.
	def next(self):
		
		if not self.hasNext():
			print("Error - End of tree reached")
			sys.exit(1)
		
		#Go to its left most child. While pushing the path to it, in the stack.
		while self.node != None:
			self.stack.append(self.node)
			self.node = self.node.left
		
		#Pop the left most child. This is the node to vist. 
		ret_node = self.stack.pop()
		self.node = ret_node
		#if visited node has right child, start the process again from right child node. 
		if self.node.right:
			self.node = self.node.right
			
		return ret_node
		
		
# https://kobra.io/#/e/-JvcI7k5w5QrTUmGITAK

"""
I tested your code and found that there're some little mistakes in it:
>>> rt = nod()
>>> lf = nod()
>>> rt.val = 1
>>> lf.val = 2
>>> ri = nod()
>>> ri.val = 3
>>> rt.left = lf
>>> ri.right = ri
>>> t = BST(rt)
>>> a = t.next()
>>> a.val
2
>>> a = t.next()
>>> a.val
2
>>> a = t.next()
>>> a.val
2

And I think the problem is that the parent of the min node is always in the stack and will not be removed
maybe you can try fetch the top of the stack and remove it every time next() is called, and do some extra work to keep the top of stack always the min value.
"""



	
		
	
