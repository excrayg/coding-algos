# Arrays

# Implement a Circular Buffer. Make sure implement:
# createCircularBuffer(int size), insertEnd(), deleteEnd(), getValue(int index)

#circular buffer. 

# 1 - 2 - 3 - 4 - 1
# have list as buffer
# have a head and tail pointer. head points to first element and 
# tail points to elem after last. 
# when is circular buffer full?
# when (tail - head) + 1 == size or 
# 0 - 1 - 2
# t   h 
# getVal(2) return a[0]
# new_idx = 1 + 2 = 3
# new_idx = 3 - 2 = 1

# (len(buf)-h ) + (t+1)
# when is circular buffer empty
# when head == tail 
# circular buffer can be inserted/deleted at end/beginning.


class circular_buffer:
    
    def __init__(self, size):
        self.head = 0
        self.tail = self.head + 1
        self.size = size
        self.buf = []
     
    def get_size(self):
        if self.head == self.tail:
            return 0
            
        if self.head < self.tail:
            return self.tail - self.head + 1
        else:
            (self.tail+1) + (self.size - self.head)
        
    def inc(self, ptr):
        ptr += 1
        if ptr == self.size:
            ptr = 0
            
        return ptr
    
    def dec(self, ptr):
        ptr -= 1
        if ptr < 0:
            ptr = self.size - 1
            
        return ptr
    
            
    def insertEnd(self, val):
        if self.get_size() == self.size:
            raise Exception("Buffer is full")
        
        self.buf[self.tail] = val
        self.tail = self.inc(self.tail)
  
    def deleteEnd(self):
        if self.get_size() == 0:
            raise Exception("Buffer is empty")
        self.tail = self.dec(self.tail)
            
    
    def getValue(self, idx):
        if idx >= self.get_size():
            raise Exception("index is greater than size")
         
        new_idx = self.head + idx
        if new_idx >= self.size:
            new_idx -= (self.size - self.head) - 1
            
        return self.buf[new_idx]
            
        
    