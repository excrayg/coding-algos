# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

#1221012
#0111222


def sort_colors(colors):
    head = 0
    tail = len(colors)-1
    cur = 0
    while cur < tail and head < tail:
        if colors[cur] == "0":
            colors[head], colors[cur] = colors[cur], colors[head]
            head+=1
            if colors[head] == colors[cur]:
                cur += 1
        elif colors[cur] == "2":
            colors[tail], colors[cur] = colors[cur], colors[tail]
            tail-=1
        else:
            cur+=1
            
    print(colors)
    
def sort_colors1(colors):
    zeros, ones, twos = 0, 0, 0
    for i in colors:
        if i == "0":
            zeros += 1
        elif i == "1":
            ones += 1
        else:
            twos += 1
            
    cur = 0
    for i in range(zeros):
        colors[cur] = 0
        cur+=1
    
    for i in range(ones):
        colors[cur] = 1
        cur+=1
    
    for i in range(twos):
        colors[cur] = 2
        cur += 1
    
    
          
c = "10"
l = list(c)
sort_colors1(l)
print(l)
sort_colors(l)

            