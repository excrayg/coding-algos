# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete at most k transactions.

# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

# [ 5, 2, 4, 6, 4 ]
# buy at lowest price and sell at highest price.
# profit should be always positive. 

#Brute force - there must be nCk ways - find 

# n < 2 k < 1 - base case
# n = 2
# [2, 4] p = 2 k = 2
# [4, 2] p = 0
# [1 2 3] - k = 2 I can buy 1 or I can buy 2 buy 1 makes sense so max profit
# [2 3 3] - 
# [1 4 2] - 
# [4 2 6]

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        n = len(prices)
        
        if n == 0 or k == 0:
            return 0
            
        if k > n/2:
            return self.m1(k, prices)
            
        local = [0]*(k+1)
        global1 = [0]*(k+1)
        res = 0
        for i in range(1, n):
            for j in range(1, k+1):
                local[j]=max(local[j]+prices[i]-prices[i-1],global1[j-1]);
                global1[j]=max(global1[j],local[j]);
                res=max(res,global1[j]);
                
        return res
        
    def m1(self, k, prices):
        res = 0
        for i in range(1, len(prices)):
            res += max(prices[i]-prices[i-1], 0)
            
        return res
        
        