#combination of phone dict lookup problem

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

#Use DFS.

def dfs_phone_dict( digits, cur_str, d, L):
    
    if digits == "":
        L.append(cur_str)
    else:
        cand = d[digits[0]]
        for c in cand:
            temp_str = cur_str+c
            dfs_phone_dict(digits[1:], temp_str, d, L)
            

d = dict()      
d["2"] = "abc"
d["3"] = "def"
L = []
dfs_phone_dict("23", "", d, L) 
print(L)
    