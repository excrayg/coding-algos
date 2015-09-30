# //Three Increasing Elements in an Array

# //Problem: Given an array of integers A, please find three indexes i, j, k, such that i<j<k and A[i]<A[j]<A[k].

#Sort the array and find the common subsequence till length 3. 
# Time start: 7:55 pm - 8:11 pm
#https://www.ics.uci.edu/~eppstein/161/960229.html

def main(s):
    
    s1 = sorted(s)
    n = len(s)+1
    lcs = [ [0]*n for i in range(n)]
    indexes = []
    for i in range(1, n):
        for j in range(1, n):
            i1 = i
            j1 = j
            if s[i1-1] == s1[j1-1]:
                lcs[i1][j1] = lcs[i1-1][j1-1] + 1
                
            else:
                lcs[i1][j1] = max(lcs[i1-1][j1], lcs[i1][j1-1])
    
    
    i = 1
    j = 1
    # n-=1
    while (i < n and j < n):
        if (s[i-1]==s1[j-1]):
    	    indexes.append(i-1)
    	    if len(indexes) == 3:
    	        print(sorted(indexes))
    	        return
    	    i+=1
    	    j+=1
    	elif lcs[i+1][j] >= lcs[i][j+1]:
    	    i+=1
    	else:
    	    j+=1
    
    print("No such indexes")
    return

s = [[4,1,2,0,3], [1,2,3,4], [4,3,2,1], [1,1,2,2,2,3], [3,1,2,2,2], [6,7,4,5,2,3]]
main(s[0])
main(s[1])
main(s[2])
main(s[5])

def findThreeInOrder(s):
    candi, first, second = s[0], 10000000, 10000000 #second > first > candi
    indc, ind1, ind2 = 0, 0, 0 #ind2 > ind1
    n = len(s)
    if (n < 3):
        return None
    for i in range(1, n): #always keep second > first >= candi, and first is always previous to second
        if (s[i] > second): #so when we meet a number that is larger than second, we come to a solution
            return (ind1, ind2, i)
        if (s[i] < candi): #save new min number and index to candi
            candi, indc = s[i], i
        elif (s[i] > candi and s[i] < first): #find a better pair of first, second so update first and second
            #this is safe because i > candi and s[i] < first < second, so it's a better pair
            first, second = candi, s[i]
            ind1, ind2 = indc, i
        elif (s[i] > first and s[i] < second): #find a better second so update second
            #this is safe because i must be greater than ind1
            second, ind2 = s[i], i
    return None
# print "findThreeInOrder"
# print findThreeInOrder(s[0])
# print findThreeInOrder(s[1])
# print findThreeInOrder(s[2])
# print findThreeInOrder(s[3])
# print findThreeInOrder(s[4])
print findThreeInOrder(s[5])

    
    