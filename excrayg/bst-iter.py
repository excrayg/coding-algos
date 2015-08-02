
#Problem: implement an external iterator for a Binary Search Tree which provides two APIs: hasNext(), next().
#Notice next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree

#inorder traversal

#Starttime1 : 3:10 pm
#endtime1:  3:35 pm

#First Attempt - Incorrect.
class BST:
	
	def __init__(self, root):
		self.node = root
		self.stack = []
		self.stack.append(root)
		fill_stack()
		
	def hasNext(self):
		if len(self.stack) > 0:
			return True
		return False
		
	def next(self):
		
		if not hasNext():
			print("Error - End of tree reached")
			sys.exit(1)
		
		if len(self.stack) == 1:
			fill_stack()
		
		n = self.stack[0]
		self.stack = self.stack[1:]
		
	def fill_stack(self):
		
		if hasNext():
			
			visit_node = self.stack[0]
			while True:
				node = visit_node.left
				if node != None:
					while node != None:
						self.stack.push(node)
						node = node.left
				else:
					visit_node = visit_node.right
					if visit_node == None:
						break
					else:
						self.stack.push(visit_node)
				
				
			
		else:
			print("Error - End of tree reached")
			sys.exit(1)
			
		

#Attempt 2 - Correct	
#starttime2 8:15 PM
#endtime2 8:30 PM

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
		
		if not hasNext():
			print("Error - End of tree reached")
			sys.exit(1)
		
		#Peek the node to visit
		node = self.stack[len(self.stack)-1]
		
		#Go to its left most child. While pushing the path to it, in the stack.
		while node.left != None:
			node = node.left
			self.stack.append(node)
		
		#Pop the left most child. This is the node to vist. 
		ret_node = self.stack.pop()
		
		#if visited node has right child, start the process again from right child node. 
		if ret_node.right:
			stack.append(ret_node.right)
			
		return ret_node
		
		
		
			


	
		
	
