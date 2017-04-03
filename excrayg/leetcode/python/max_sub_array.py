# // Given a 2D array, find the maximum sum subarray in it. For example, in the following 2D array, the maximum sum subarray is highlighted with blue rectangle and sum of this subarray is 29.

# // http://www.geeksforgeeks.org/wp-content/uploads/rectangle.png

# // This problem is mainly an extension of Largest Sum Contiguous Subarray for 1D array.

# // time: from 9:20 to 9:46, no idea except for brute force or divide&conquer and brute force

# // brute force
# // btw, the answer of the image is not right, the largest sum shoud be the rectangle from (0,1) to (3,3)


def find_1d_sum(m):
    max_sum = float("-inf")
    curr_sum = 0
    for i in m:
        curr_sum += i
        if curr_sum < 0:
            curr_sum = 0
        if curr_sum > max_sum:
            max_sum = curr_sum
            
    return max_sum

def find_max_sum(mat):
    max_sum = float("-inf")
    nrows = len(mat)
    ncols = len(mat[0])
    for i in range(ncols):
        t = [0]*nrows
        for j in range(i, ncols):
            for k in range(nrows):
                t[k] += mat[k][j]
                
            sum1 = find_1d_sum(t)
            if sum1 > max_sum:
                max_sum = sum1
            
    return max_sum
    
nrows = 4
ncols = 5
mat = [[0]*ncols for i in range(nrows)]
mat = [[1,2,-1,4,-20], 
        [8,-3,4,2,1], [3,8,10,-8,3], [-4,-1,1,7,-6]]
#print(find_1d_sum(mat[0]))
print(find_max_sum(mat))