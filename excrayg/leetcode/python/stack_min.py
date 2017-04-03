Stack with Function min()

Problem: Define a stack, in which we can get its minimum number with a function min. In this stack, the time complexity of min(), push() and pop() are all O(1).

#have two stacks, one is the usual stack. one is the min stack
#min would contain the minimum till that sequence. 
#For instance if stack is 4(top), 1, 3, 2. Min would be 1(top), 1, 2, 2. Pushing/Popping usual stack, you should do it in min stack too. 

class Stack:
	def __init(self):
		self.stack = []
		self.min_stack = []
		
	def push(self, val):
		self.stack.append(val)
		if len(min_stack) == 0:
			self.min_stack.append(val)
		else:
			current_min = self.min_stack[len(min_stack)-1]
			if val < current_min:
				self.min_stack.append(val)
			else:
				self.min_stack.append(current_min)
	
	def pop(self):
		self.min_stack.pop()
		return self.stack.pop()
	
	def min(self):
		if len(stack) != 0:
			return self.min_stack[len(min_stack)-1] #I guess min() doesnt require a pop. 
		else:
			print("No elems in stack")
			