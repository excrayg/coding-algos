# Given an array arr, return the number of qaz pairs.
# We define a qaz pair as a pair (m, n) such that m < n but arr[m] > arr[n]. 

# Example:
# arr = [1,4,5,3,2]
# qaz pairs:
# [4,2], [4,3], [5,3], [5,2], [3,2]

# Return 5

# Hint: Complexity we are looking for is O(nlogn)


#brute force, check for every ordered pair. 
# divide and conquer
# [4,5,3,2]
# [4,5] [3,2]
# do merge sort
# [4,5] [2,3]
# count number of unordered pairs in left and right
# num_unordered_pair = nl + nr + count bw them. 

def num_qaz_pairs(arr):
    if len(arr) == 1:
        return arr, 0
    m = len(arr)/2
    # print(arr)
    arr_l, nl = num_qaz_pairs(arr[:m])
    arr_r, nr = num_qaz_pairs(arr[m:])
    arr, ct = num_qaz_in_merged_arr(arr_l, arr_r)
    return arr, nl + nr + ct
    
def num_qaz_in_merged_arr(left_arr, right_arr):
    
    i = len(left_arr) - 1
    j = len(right_arr) - 1
    
    temp = []
    count = 0
    # # [4,5], [2,3]
    # while i >= 0 and j >= 0 :
    #     if left_arr[i] < right_arr[j]:
    #         i-=1
    #     else:
    #         count += 1
    #         j-=1
    #         # break
        
    i = 0
    j = 0
            
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            temp.append(left_arr[i])
            i+=1
        else:
            temp.append(right_arr[j])
            count += len(left_arr) - i
            j+=1
            
    if i == len(left_arr):
        temp.extend(right_arr[j:])
    else:
        temp.extend(left_arr[i:])
    
    # print(left_arr, right_arr, temp, count)
   
    return temp, count
    

arr = [1,4,5,3,2]
print(num_qaz_pairs(arr)[1])

arr = [5,4,3,2]
print(num_qaz_pairs(arr)[1])