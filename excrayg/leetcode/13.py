# Question:
# Given a string S, find the longest palindromic substring in S. You may assume that the
# maximum length of S is 1000, and there exists one unique longest palindromic substring.

def find_largest_palindrome(st):
    n, nr = find_odd_palindrome(st)
    m, mr = find_even_palindrome(st)
    
    print(n,m)
    if n > m:
        print(st[nr[0]:nr[1]+1])
    else:
        print(st[mr[0]:mr[1]+1])
        

def find_odd_palindrome(st):
    n = len(st)
    cp = 1
    end = n - 1
    ml = float("-inf")
    mr = [None, None]
    while cp < end:
        i = cp-1
        j = cp+1
        while st[i] == st[j] and i >= 0:
            l = (j - i) + 1
            if l > ml:
                ml = l
                mr[0] = i
                mr[1] = j
            i -= 1
            j += 1
        cp += 1
        
    return ml, mr
    
def find_even_palindrome(st):
    ml = float("-inf")
    mr = [0, 1]
    
    return ml, mr
    
print(find_largest_palindrome("abcabcf"))
            
    