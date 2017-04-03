

#abcabcbb - abc
#bbb - b

# have an array of a-z. record the position. 

st = "bbb"
record_char = [None]*26
si = 0
max_range = [None, None]
max_len = float("-inf")
n = len(st)
cp = 0
cur_len = 0
while cp < n:
    p = ord(st[cp])-ord('a')
    if record_char[p] != None:
        si = record_char[p] + 1
    else:
        record_char[p] = cp
        cur_len = (cp - si) + 1
        if cur_len > max_len:
            max_len = cur_len
            max_range[0] = si
            max_range[1] = cp
            
    cp += 1
    
print(st[max_range[0]:max_range[1]+1])
    
