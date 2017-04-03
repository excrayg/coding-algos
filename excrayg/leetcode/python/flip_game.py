
# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip twoconsecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
# Write a function to compute all possible states of the string after one valid move.
# For example, given s = "++++", after one move, it may become one of the following states:
# [
#   "--++",
#   "+--+",
#   "++--"
# ]
# If there is no valid move, return an empty list [].

def flip(s):
    n = len(s)
    l = list(s)
    res = []
    for i in range(n):
        head = ""
        tail = ""
        if i != n-1 and l[i] == '+' and l[i+1] == '+':
            if i != 0:
                head = s[:i]
            if i+2 < n:
                tail = s[i+2:]
            res.append(head+"--"+tail)
            
    return res
    
print(flip("++++"))
            


