import heapq

def insert(num): 
    
    global N
    # print(N)
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
    elif N%2 == 1:
        min_heap_elem = -1*heapq.heappushpop( maxHeap, -1*num ) 
        heapq.heappush( minHeap, min_heap_elem ) 
        N+=1

def getMedian():
    
    # print(N)
    
    if N%2==0: 
    	return (-1*maxHeap[0]+minHeap[0])/2.0 
    else: 
    	return -1*maxHeap[0] 



minHeap, maxHeap = [], [] 
N=0   
	
a = [3,1,2]
for i in a:
    insert(i)

b = [6,5,4]
for i in b:
    insert(i)

print(getMedian())