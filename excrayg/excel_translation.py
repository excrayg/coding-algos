# translate a given number to the column title of excel.
# e.g.: 0~A, 1~B, .. 25~Z, 26~AA, etc.
# test cases: 0, 1, 25, 26, 51, 52, 675~ZZ, 676~AAA
# Z * 26 ^0 + Z * 26 ^ 1 = 25 + 25*26

s = ""
for i in range(ord('a'), ord('z')+1):
    s+=chr(i)
    
print(s)
def toString(n):
    if n / 26 == 0:
        return s[n%26]
    else:
        t = ""
        c = n / 26 - 1 if n%26 == 0 else n/26
        
        t += toString(c) + s[n%26]
        return t

print(toString(52))
print(t
oString(675))
print(toString(676))