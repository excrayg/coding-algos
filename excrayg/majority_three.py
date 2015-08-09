# // problem: given an array of n numbers, find the numbers that appears more than floor(n/3) times in the array.
# // e.g.: [1,2] returns [1,2] and [1,1,2] returns 1 and [1,2,3] returns []

l = [1,1,2]
max_times = int(len(l)/3)
op = set()
for i in l:
    if l.count(i) >= max_times:
        op.add(i)
        
print(op)

# neat solution! You count every element in l, which makes the time complexity O(mn).
# can you do it better in O(n) time and O(1) space?
# I am not able to think of  something without doing sort or hashmap for this. Any clues?
# below is a demo of majority two, you can think of a similar method

num = 0; count = 0
for i in l:
    if count == 0:
        num = i
    elif i == num:
        count+=1
    else:
        count-=1
count = 0
n = len(l)
n /= 2
for i in l:
    if num == i:
        count+=1
if count > n:
    return num
return None