#Find k in 2 sorted arrays in O(logk) time. 

# a - 1 3 4 5 7
# b - 2 6 8 9 10

# m = len(a) / 2
# n = len(b) / 2

# k = 7

# if k > a[m] a[m] < b[n] k lies somewhere bw a[m+1]..b[n-1]
#             a[m] > b[n] k lies somewhere bw a[m+1]..b[n+1]

# if k < a[m] if a[m] < b[n] k lies somewhere bw a[0:m-1]..b[0:n-1]
#                a[m] > b[n] k lies somewhere bw a[0:m-1]..b[


#base case

# if a[m] == k : return m
# if a[0], b[0] , if k == a[0] or k == b[0]

# if k > a[m] and k > b[n] 
# k lies between a[m+1] and b[n+1]

# if k < a[m] and k > b[n]
# k lies between a[:m-1]..b[n+1..]

# if k  > a[m] and k < b[n]
# k lies between a[m+1:]..b[:n-1]

# if k < a[m] and k < b[n]
# k lies between a[:m-1]..b[:n-1]

def find_in_two_sorted_arr(a, b, k):
    print(a, b)
    if len(a) == 0:
        return k in b
        
    if len(a) > len(b):
        return find_in_two_sorted_arr(b,a,k)
        
    if len(a) == 1 and len(b) == 1:
        if k == a[0] or k == b[0]:
            return True
            
    m = len(a) / 2
    n = len(b) / 2
    
    if a[m] == k or k == b[n]:
        return True
        
    if k > a[m] and k > b[n]:
        return find_in_two_sorted_arr(a[m+1:], b[n+1:], k)
    elif k > a[m] and k < b[n]:
        return find_in_two_sorted_arr(a[m+1:], b[:n], k)
    elif k < a[m] and k > b[n]:
        return find_in_two_sorted_arr(a[:m], b[n+1:], k)
    elif k < a[m] and k < b[n]:
        return find_in_two_sorted_arr(a[:m], b[:n], k)
    
    print("Should not come here")
    return None

a = [1, 3, 4, 5, 7]
b = [2, 6, 8, 9, 10]

print(find_in_two_sorted_arr(a, b, 1))
print(find_in_two_sorted_arr(a, b, 3))
print(find_in_two_sorted_arr(a, b, 9))
print(find_in_two_sorted_arr(a, b, 10))
print(find_in_two_sorted_arr(a, b, 11))


    

