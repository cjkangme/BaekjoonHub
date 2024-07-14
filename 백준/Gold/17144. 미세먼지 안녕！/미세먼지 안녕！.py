import sys
from copy import deepcopy

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def is_cleaner(x, y, row_cleaner):
    if (x == row_cleaner or x == row_cleaner-1):
        if y == 0:
            return True
    return False

def diffuse(board, row_cleaner):
    next_board = deepcopy(board)
    
    for x in range(R):
        for y in range(C):
            dust = board[x][y]
            if dust < 5:
                continue
            
            amount_diffuse = dust // 5
            for i in range(4):
                xx = x + dx[i]
                yy = y + dy[i]
                if 0<=xx<R and 0<=yy<C and not is_cleaner(xx, yy, row_cleaner):
                    next_board[xx][yy] += amount_diffuse
                    next_board[x][y] -= amount_diffuse
                
    return next_board

def blow(board, row_cleaner):
    # 위쪽
    for x in range(row_cleaner-1, 0, -1):
        board[x][0] = board[x-1][0]
    for y in range(C-1):
        board[0][y] = board[0][y+1]
    for x in range(row_cleaner-1):
        board[x][-1] = board[x+1][-1]
    for y in range(C-1, 1, -1):
        board[row_cleaner-1][y] = board[row_cleaner-1][y-1]
    board[row_cleaner-1][1] = 0
    # 아래쪽
    for x in range(row_cleaner, R-1):
        board[x][0] = board[x+1][0]
    for y in range(C-1):
        board[-1][y] = board[-1][y+1]
    for x in range(R-1, row_cleaner, -1):
        board[x][-1] = board[x-1][-1]
    for y in range(C-1, 1, -1):
        board[row_cleaner][y] = board[row_cleaner][y-1]
    board[row_cleaner][1] = 0
    return board

if __name__=="__main__":
    R, C, T = map(int, input().split())
    # 공기청정기 아래쪽 행 위치, 총 미세먼지 양
    row_cleaner, total = -1, 0
    board = [[0] * C for _ in range(R)]
    
    for i in range(R):
        row = list(map(int, input().split()))
        if row[0] == -1:
            row_cleaner = i
        for j in range(C):
            dust = row[j]
            board[i][j] = dust
            total += dust
    total += 2 # 공기청정기가 -1이므로 보정
    for _ in range(T):
        board = diffuse(board, row_cleaner)
        board = blow(board, row_cleaner)
        total -= board[row_cleaner-1][0]
        total -= board[row_cleaner][0]
        board[row_cleaner-1][0] = 0
        board[row_cleaner][0] = 0
    print(total)
