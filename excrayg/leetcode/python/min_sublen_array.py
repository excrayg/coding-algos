#13. 9 - Let A and Q be arrays of strings. Define subarray A[i:j] to cover Q if for all k belongs to [Q, n_q-1], where n_q is length of Q, there exists l belongs [i,j], Q[k] = A[l]
#Write a function that takes two arryas A and Q and computes a minimum length subarray A[i:j] that covers Q. 
# Suppose A is presented in streaming fashopn and Q can be stored in RAM. 

def find_cover(A, Q):
    from collections import defaultdict
    needs_to_find = defaultdict(int)
    has_found = defaultdict(int)
    for v in Q:
        needs_to_find[v] += 1
    start = 0
    end = 0
    count = 0
    min1 = float("inf")
    while end < len(A):
        if A[end] not in needs_to_find:
            end+=1
        else:
            has_found[A[end]] += 1
            if needs_to_find[A[end]] >= has_found[A[end]]:
                count += 1
            if count == len(Q):
                min1 = min(min1, (end-start)+1)
                while A[start] not in needs_to_find or has_found[A[start]] > needs_to_find[A[start]]:
                    start += 1
                    min1 = min(min1, (end-start)+1)
                    if A[start] in needs_to_find:
                        has_found[A[start]] -= 1
            end+=1
            
    return min1
    
A = ["d", "e", "f", "g", "f", "h","i", "t"]
Q = ["g", "t", "f", "f", "h"]

print(find_cover(A, Q))
    