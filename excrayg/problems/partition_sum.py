# // Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

# // Examples

# // arr[] = {1, 5, 11, 5}
# // Output: true 
# // The array can be partitioned as {1, 5, 5} and {11}

# // arr[] = {1, 5, 3}
# // Output: false 
# // The array cannot be partitioned into equal sum sets.

# // time: from 9:06 to 9:40

#sorting solution

def partition(arr):
    arr = sorted(arr)
    for i in range(1, len(arr)):
        if sum(arr[0:i])==sum(arr[i:]):
            return True
    return False
    
print(partition([1,5,11,5]))

#effecient better than o(nlogn)?