

def find_max_min(ip):
    if len(ip) ==1:
        return int(ip[0])
        
    val1 = float("-inf")
    # val2 = float("inf")
    for i in range(1, len(ip), 2):
        if ip[i] == '+':
            val1 = max(val1, find_max_min(ip[:i]) + find_max_min(ip[i+1:]))
        else:
            val1 = max(val1, find_max_min(ip[:i]) - find_max_min(ip[i+1:]))
            
    return val1
    

print(find_max_min("1+3−2−5+1−6+7")) # 1+3−+7=4-


# status: m[i][j] means the max sum between i,j?
# m[i][j] = max(m[i][i+2k] op m[i+2k][j])
# for i in range(1, len(ip)):
#   for j in range(0, len(ip) - i):
#     for k in range(0, i):
#       m[j][j+i] = max(m[j][j+k] op  

#memoization is easy with start and end index as key
#how to conver this to dynamic
#n^2 table?