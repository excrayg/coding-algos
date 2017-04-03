# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

# For example,
# Given the following matrix:

# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# You should return [1,2,3,6,9,8,7,4,5].

# single row, single col, 2 x2 

def print_spiral( mat ):
    nr = len(mat)
    nc = len(mat[0])
    
    nr_t = nr
    cur = 0
    l = []
    while cur <= nr/2 and cur <= nc/2 :
        print_sub(mat, cur, nr_t, nc, l)
        nc -= 1
        nr_t -= 1
        cur += 1
    
    return l
        
def print_sub(mat, cur_row, nr, nc, l):
    
    #print from left to right
    for i in range(cur_row, nc):
        l.append( mat[cur_row][i] )
        
    #print last column
    if nr - cur_row > 1:
        for i in range(cur_row+1, nr):
            l.append( mat[i][nc-1] )
    
    #print last row
    cur_col  =  nc-2
    if cur_row - cur_col > 0:
        for i in range(cur_col, cur_row-1, -1):
            l.append( mat[nr-1][i] )
            
    #print first column
    if (nr - 2) - cur_row > 0:
        for i in range( nr-1, cur_row, -1):
            l.append( mat[i][cur_row] )
            

mat =  [ [ 1, 2, 3 ],
         [ 4, 5, 6 ],
         [ 7, 8, 9 ]]

print(print_spiral(mat))
    
            
