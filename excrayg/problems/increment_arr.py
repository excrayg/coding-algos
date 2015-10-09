#  //Given an array a contains all digits 0-9 a   = [1, 4, 2, 1] # which represents 1421 Add one to the number and return the array return a = [1, 4, 2, 2] # which represents 1422 . Identify all corner cases. 

# // cases: 0, 1, 9, 10, 11, 19, 29, 99, 999, 999999999, 1999999999, 

def inc_arr(arr):
    l = len(arr)
    t = l-1
    while t >= 0:
        if arr[t] == 9:
            arr[t] = 0
        else:
            arr[t]+=1
            break
        t-=1
    else:
        arr.insert(0,1)
    return arr
    
print(inc_arr([1]))
print(inc_arr([9]))

