

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
    
def length_list(node):
    _len = 0
    while node != None:
        node = node.next
        _len+=1
        
    return _len
    
