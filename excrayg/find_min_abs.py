# given an sorted array, find the number that has the min absolute value.
# e.g.: [-2, -1, 2] return -1. do it in O(logn) time.

#binary search. check middle element, if its positive, it is less than right element, go to left half, if it is negative, then abs(x) >= right, go to right half,
#abs(x) < right, go to left half, 
#boundary if l-r > 0, l points to element. 



def find_abs(a):
    l = 0
    r = len(a)-1
    
    while r-l > 1:
        m = l + int((r-l)/2)
        
        # print(l,m,r)
        if a[m] > 0:
            r = m-1
        else:
            if abs(a[m]) >= abs(a[r]):
                l = m
            else:
                r = m
      
    print(a[r])
    
a = [-4, -3, -2, -1]
find_abs(a)
a = [1]
find_abs(a)
a = [-1, 11, 12, 13]
find_abs(a)
a = [1, 11, 12, 13]
find_abs(a)
