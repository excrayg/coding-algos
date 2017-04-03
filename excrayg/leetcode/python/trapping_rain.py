# //https://leetcode.com/problems/trapping-rain-water/

def find_trap_water_helper(arr, i, stack):
    #find index such that arr[i]>arr[i+1]
    while i+1 < len(arr) and arr[i] < arr[i+1]:
        i+=1
        
    if i > len(arr)-1:
        return len(arr), 0
        
    
    area = 0
    
    stack.append((arr[i], i))
    i+=1
    while i < len(arr) and len(stack) != 0:
        top = stack[-1][0]
        
        while i < len(arr) and arr[i] <= top:
            if arr[i] < top:
                stack.append((arr[i], i))
                top = stack[-1][0]
            i+=1
            
        if i == len(arr):
            return len(arr), 0
            
        while i < len(arr) and len(stack) != 0:
            right_end = arr[i]
            base = stack.pop()[0]
            left_end = stack.pop()
            if left_end[0] <= right_end:
                height = left_end[0] - base
                width = i - left_end[1]-1
                area += height * width
                
                if len(stack) != 0:
                    stack.append((left_end[0], i))
            else:
                #you keep left_end in stack and insert new base.
                height = right_end - base
                width = i - left_end[1]-1
                area += height * width
                stack.append(left_end)
                stack.append((right_end, i)) #right_end is new base
                i+=1
            
    
    return i, area
        
    #height = max(left_end[0], right_end)
    #height -= base
    #width = i - left_end[1]-1
    #area += height * width
    
    

def find_trap_water(arr):
    i = 0
    total_trap_water = 0
    stack = []
    while i < len(arr):
        i, t = find_trap_water_helper(arr, i, stack)
        total_trap_water += t
    return total_trap_water

arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(find_trap_water(arr))

