# There are N children standing in a line. Each child is assigned a rating value.

# You are giving candies to these children subjected to the following requirements:

# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# eg 1: 1 2 3 2 1
# eg 2: 3 2 1 2 3

# eg 1: 2 4 7 6 3
# normalize this 
# left and right partial array with how many greater till at this index
# 0 1 2 0 0 
# 0 0 2 1 0    

# 1 2 3 2 1

# eg 2: 9 7 2 8 10
# 0 0 0 1 2 
# 2 1 0 0 0 

class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        n = len(ratings)
        left_candy = [0] * n
        right_candy = [0] * n
        
        for i in range(1, n):
            prev = ratings[i-1]
            if ratings[i] > prev:
                left_candy[i] = left_candy[i-1] + 1
            
        for i in range(n-2, -1,  -1):
            next1 = ratings[i+1]
            if ratings[i] > next1:
                right_candy[i] = right_candy[i+1] + 1
                
        min_cand = 0
        for i in range(n):
            min_cand += max(left_candy[i], right_candy[i]) + 1
            
        return min_cand
        
print(Solution().candy([2, 4, 7, 6, 3]))
        
        
        
        
        
        