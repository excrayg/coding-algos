# Given a list, rotate the list to the right by k places, where k is non-negative.

# For example:
# Given 1->2->3->4->5->NULL and k = 2,
# return 4->5->1->2->3->NULL.

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        n = 0
        t = head
        while t:
            n += 1
            t = t.next
            
        k = k % n
        p1 = head 
        p2 = head
        
        t1 = k
        while t1:
            p2 = p2.next
            t1 -= 1
        
        p = None
        while p2:
            p = p1
            p1 = p1.next
            p2 = p2.next
            
        h = p1
        p.next = None
        
        t = h
        p = None
        while t:
            p = t
            t = t.next
            
        p.next = head
        
        return h
        
def PrintList(  head ):
    while head:
        print(head.val)
        head = head.next

h1 = ListNode(1)
h2 = ListNode(2)
h3 = ListNode(3)
h4 = ListNode(4)
h5 = ListNode(5)

h1.next = h2
h2.next = h3
h3.next = h4
h4.next = h5

PrintList(Solution().rotateRight(h1, 2))