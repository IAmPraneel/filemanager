def is_safe(board,row,col,n):

    # check same row (left side)
    for j in range(col):
        if board[row][j]==1:
            return(False)
    #check same column (upwards)
    for i in range(row):
        if board[i][col]==1:
            return(False)
        
    # Check left diagnonal (upper-left)
    i = row - 1
    j = col - 1
    while i >=0 and j>=0:
        if board[i][j]==1:
            return(False)
        i-=1
        j-=1
    # Check right diagonal (upper-right)
    i = row-1
    j = col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return(False)
        i-=1
        j+=1

    return(True)

def solve(board,row,n):
    if row == n:
        for i in range(n):
            print(board[i])
        print()
        return
    
    for col in range(n):
        if is_safe(board,row,col,n):
            board[row][col] = 1 # place queen
            solve(board,row+1,n)# Move to next row
            board[row][col] = 0 # backtrack

print("Enter number of queens: ")
n = int(input())
board = []

for i in range(n):
    row = []
    for j in range(n):
        row.append(0)
    board.append(row)

solve(board,0,n)
