# // Merge n sorted link list
#use a heap, push n "first" elements into heap, pop
import heapq


class node:
    def __init__(self, val):
        self.val = val
        self.next = None

def create_list(start_idx, _len):
    head = None
    prev = None
    for i in range(start_idx, _len):
        temp = node(i)
        if head == None:
            head = temp
        if prev == None:
            prev = temp
        else:
            prev.next = temp
            prev = temp
            
    return head
    
    
def print_list(node):
    temp = node
    while temp != None:
        print temp.val,
        print "->",
        temp = temp.next
    print "None" 
       
       
num_lists = 10
t = []
for i in range(num_lists):
    t.append(create_list(i*num_lists, num_lists)
    
#insert to heap (elem, listnum) tuple

        