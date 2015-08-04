# //Median in Stream

# //Question: How to get the median from a stream of numbers at any time? The median is middle value of numbers. If the count of numbers is even, the median is defined as the average value of the two numbers in middle.

# //Please note that this is a stream of numbers, hence the number of numbers keeps increasing dynamically. And they are not necessarily sorted. 

#Need two heap.
#n/2 numbers stored in max heap and n/2 numbers stored in min_heap. If n is even, average of min_root and max_root, else max_root. 