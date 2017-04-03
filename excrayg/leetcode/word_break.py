# Given a string s and a dictionary of words dict, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# For example, given
# s = "leetcode",
# dict = ["leet", "code"].

# Return true because "leetcode" can be segmented as "leet code".

class Solution:
     # param s, a String 
    # param dict, a set of String 
    # return a boolean 
    # !good Coding 
    def wordBreak (self, s, dict):
        dp = [False for i in range (len (s) +1 )]
        dp [0] = True
        for i in range (1, len (s) +1 ):
            for k in range (i):
                if dp [k] and s [k: i] in dict:
                    dp [i] = True
        return dp [len (s)]
        

s = Solution()
str = "leetcode"
w = {"leet", "code"}

print(s.wordBreak(str, w))

str = "aaaaaaa"
w = {"aaaa","aa"}

print(s.wordBreak(str, w))

        
        