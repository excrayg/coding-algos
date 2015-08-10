# translate a given number to the column title of excel.
# e.g.: 0~A, 1~B, .. 25~Z, 26~AA, etc.
# test cases: 0, 1, 25, 26, 51, 52, 675~ZZ, 676~AAA
# Z * 26 ^0 + Z * 26 ^ 1 = 25 + 25*26


#a - 0, z - 25, ba - 52, zz - 675
#a -z - n%26 ba >    (2-1)%26 + [52%26]
# 17575, 17576 = 26^3


#ba  - (2-1)%26 + [52%26 == 0 ] //if prev n % 26 == 0, then in base case you need to subtract 1. 
#zz   - (25)%25 + [675%26 == 25]
#aaa - (0) % 26 + (26) % 26 + [676%26]
s = ""
for i in range(ord('a'), ord('z')+1):
    s+=chr(i)
    
print(s)
def toString(n, i):
    print(n)
    if n / 26 == 0:
        #the flag i would have the reverse logic of flag i in line 23. 
        if i == 0:
            return s[(n-1)%26]
        else:
            return s[n%26]
    else:
        t = ""
        i = 0 if n%26 == 0 else 1
        t += toString(n/26, i) + s[n%26]
        return t

print(toString(52, 1))
print(toString(675, 1))
print(toString(676, 1))

def trans(n):
    res = ""
    while (n>=0):
        res = s[n%26] + res;
        n/=26;
        n -= 1;
    return res;
    