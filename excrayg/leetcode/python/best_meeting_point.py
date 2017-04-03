# [LeetCode] Best Meeting Point

# Problem Description:

# A group of two or more people wants to meet and minimize the total travel distance. You are given a 2D grid of values 0 or 1, where each 1 marks the home of someone in the group. The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

# For example, given three people living at (0,0), (0,4), and (2,2):

# 0 - 0 - 1 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 0 - 0 - 0
# |   |   |   |   |
# 0 - 0 - 0 - 1 - 0
# The point (0,2) is an ideal meeting point, as the total travel distance of 2+2+2=6 is minimal. So return 6.

#for 1D, it will be manhattan distance / 2

def best_meeting_pt( grid ):
    
    ll = []
    jj = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                ll.append(i)
                jj.append(j)
                
    jj.sort()
    # print(jj)
    c = len(grid)
    lo = ll[c/2]
    jo = jj[c/2]
    
    s = 0
    for i in ll:
        s += abs(i-lo)
        
    for j in jj:
        s += abs(j-jo)
        
    return s
        
    
grid = [ [1, 0, 0, 0, 1], 
         [0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0] ]
         
print( best_meeting_pt(grid) )
                