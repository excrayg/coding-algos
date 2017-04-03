

# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color.
# Return the total number of ways you can paint the fence.
# Note:
# n and k are non-negative integers.

# rg gr rb br gb bg

# rgr grg brb rbr gbg bgb 
# rgb gbr bgr rbg grb brg

# n = 3 k = 2
#    1  2 3
# 1  1  2 3
# 2  0  2 6
# 3  0  2 

def paint_fence( n , k):
    grid = [ [0] * k for i in range(n) ]
    for i in range(k):
        grid[0][i] = i+1
    for i in range(1, n):
        for j in range(1, k):
            m = grid[i-1][j]
            t = grid[i][j-1]
            if m == 0:
                m = 1
            if t == 0:
                t = 1
            
            grid[i][j] = m*t
        
    # print(grid)
    # print(n, k)
    return grid[n-1][k-1]
    
print(paint_fence(3,2))
print(paint_fence(3,3))
            