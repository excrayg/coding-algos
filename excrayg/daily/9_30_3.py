#Write a function that takes an array of integers A and returns the length of a longest subarray of A with the constraint that all its elements are distinct. 
# For eg. A = [5,7,5,11,13,2,11,19,2,11], longest subarray with distinct elements is A[1:5]

def find_longest_subarray(A):
    start = 0
    end = 0
    pos_map = dict()
    max1 = 0
    while end < len(A):
        el = A[end]
        if el not in pos_map:
            pos_map[el] = end
            max1 = max(max1, (end-start)+1)
        else:
            start = pos_map[el] + 1
            pos_map[el] = end
        end+=1
            
    return max1
        
A = [5,7,5,11,13,2,11,19,2,11]
print(find_longest_subarray(A))
        