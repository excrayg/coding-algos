#Write a function that takes as input a postitive integer n, and returns a list of all distinct nonattacking placements of n queens on nxn chess board.

#0,0 0,1 0,2
#1,0 1,1 1,2
#
from pprint import pprint

def is_valid(n, row, col, board):
    for i in range(n):
        if i != col and board[row][i] == "Q":
            return False
    else:
        for i in range(n):
            if i != row and board[i][col] == "Q":
                return False
        else:
            i = row-1
            j = col-1
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i-=1
                j-=1
            i = row + 1
            j = col + 1
            while i < n and j < n:
                if board[i][j] == "Q":
                    return False
                i+=1
                j+=1
            i = row - 1
            j = col + 1
            while i >= 0 and j < n:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j += 1
            i = row + 1
            j = col - 1
            while i < n and j >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1
            return True
            
                
            

def n_queen(n, row, board):
    if n == 0:
        # pp = pprint.PrettyPrinter(indent=4)
        for i in range(len(board)):
            pprint(board[i])
        print("_____________")
    else:
        for i in range(len(board)):
            if is_valid(len(board), row, i, board):
                board[row][i] = "Q"
                n_queen(n-1, row+1, board)
                board[row][i] = 0
                
n = 8
board = [[0]*n for i in range(n)]
n_queen(n, 0, board)
            