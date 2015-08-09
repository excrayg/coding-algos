# //Median in Stream

# //Question: How to get the median from a stream of numbers at any time? The median is middle value of numbers. If the count of numbers is even, the median is defined as the average value of the two numbers in middle.

# //Please note that this is a stream of numbers, hence the number of numbers keeps increasing dynamically. And they are not necessarily sorted. 

#Need two heap.
#n/2 numbers stored in max heap and n/2 numbers stored in min_heap. If n is even, average of min_root and max_root, else max_root. 

import heapq

def insert(num): 
    
    global N
    print(N)
    if N%2==0: 
        
    	heapq.heappush(maxHeap, -1*num) 
    	N+=1 
    
        if len(minHeap)==0: 
        	return 
        
        if -1*maxHeap[0]>minHeap[0]: 
        	min_heap_elem = -1*heapq.heappop(maxHeap) 
        	max_heap_elem = heapq.heappop(minHeap)   
        	heapq.heappush( maxHeap, -1*max_heap_elem ) 
        	heapq.heappush( minHeap, min_heap_elem ) 
	
	else: 
        min_heap_elem = -1*heapq.heappushpop( maxHeap, -1*num ) 
        heapq.heappush( minHeap, min_heap_elem ) 
        N+=1


def getMedian():
    
    print(N)
    
    if N%2==0: 
    	return (-1*maxHeap[0]+minHeap[0])/2.0 
    else: 
    	return -1*maxHeap[0] 



minHeap, maxHeap = [], [] 
N=0   
	
a = [1,2,3]
for i in a:
    insert(i)

print(getMedian())