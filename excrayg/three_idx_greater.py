# //Three Increasing Elements in an Array

# //Problem: Given an array of integers A, please find three indexes i, j, k, such that i<j<k and A[i]<A[j]<A[k].

#Sort the array and find the common subsequence till length 3. 
# Time start: 7:55 pm - 8:11 pm

def main(s):
    
    s1 = sorted(s)
    n = len(s)+1
    lcs = [ [0]*n for i in range(n)]
    length_s = set()
    indexes = []
    for i in range(1, n):
        for j in range(1, n):
            i1 = i-1
            j1 = j-1
            if s[i1] == s1[j1]:
                lcs[i1][j1] = lcs[i1-1][j1-1] + 1
                if(lcs[i1][j1] not in length_s):
                    length_s.add(lcs[i1][j1])
                    indexes.append(i1)
                if len(indexes)==3:
                    print(sorted(indexes))
                    return
            else:
                lcs[i1][j1] = max(lcs[i1-1][j1], lcs[i1][j1-1])
    
    print("No such indexes")
    return

s = [[4,1,2,0,3], [1,2,3,4], [4,3,2,1]]
main(s[0])
main(s[1])
main(s[2])
            