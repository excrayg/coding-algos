# given a root of a linked list, reverse it. 
# add-on: what if the list has a cycle?

#if it has cycle, find start of cycle and number of nodes in it, then reverse it


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
    
def rev_list(node):
    prev = None
    while node.next:
        n = node.next
        node.next = prev
        prev = node
        node = n
        
    node.next = prev
    return node

def print_list(node):
    temp = node
    while temp != None:
        print temp.val,
        print "->",
        temp = temp.next
    print "None" 
    
print_list(rev_list(create_list(0,10)))
