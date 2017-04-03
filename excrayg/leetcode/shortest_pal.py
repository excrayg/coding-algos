# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

# For example:

# Given "aacecaaa", return "aaacecaaa".

# Given "abcd", return "dcbabcd".

#     ccbaabc

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        n = len(s)
        if n == 0 or n == 1:
            return s
            
        mid = n/2
        res = ""
        i = mid
        while i >= 1:
            
            if s[i] == s[i-1]:
                res = self.scan(s, i, i-1)
                if res != "":
                    return res
            else:
                res = self.scan(s, i-1, i-1)
                if res != "":
                    return res
            i-=1
            
        return res
        
    def scan(self, s, l, r):
        
        i = 1
        while l - i >= 0:
            if s[l-i] != s[r+i]:
                break
            i+=1
            
        if l-i >= 0 :
            return ""
            
        rev = s[r+i:][::-1]
        return rev+s
        
        
s = Solution()
print(s.shortestPalindrome("abcd"))
print(s.shortestPalindrome("aacecaaa"))