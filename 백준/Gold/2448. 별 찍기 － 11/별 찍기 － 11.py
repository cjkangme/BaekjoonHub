import sys
from collections import deque

input = sys.stdin.readline

def find_k(N):
    N //= 3
    k = 0
    while N > 1:
        N //= 2
        k += 1
    return k

def find_m(k):
    m = 5
    for _ in range(k):
        m *= 2
        m += 1
    return m

def set_board(board, que, row, col):
    if board[row][col] == " ":
        board[row][col] = "*"
        que.append((row, col))

def make_board(board, N, M):
    start = M//2
    board[0][start] = "*"
    que = deque()
    que.append((0, start))
    
    while que:
        row, col = que.popleft()
        # 트리가 완성되었으면 break
        if row >= N:
            break
        
        if row % 3 == 0:
            set_board(board, que, row+1, col-1)
            set_board(board, que, row+1, col+1)
        elif row % 3 == 1:
            set_board(board, que, row+1, col-1)
            set_board(board, que, row+1, col)
            set_board(board, que, row+1, col+1)
        else:                                        
            try:
                if board[row-1][col-1] == " " and board[row-1][col+1] == "*":
                    if board[row][col-2] == " ":
                        set_board(board, que, row+1, col-1)
                        continue
                if board[row-1][col-1] == "*" and board[row-1][col+1] == " ":
                    if board[row][col+2] == " ":
                        set_board(board, que, row+1, col+1)
            except:
                continue
            

if __name__=="__main__":
    N = int(input())
    k = find_k(N)
    M = find_m(k)
    board = [[" " for _ in range(M)] for _ in range(N)]
    make_board(board, N, M)

    for i in range(N):
        print("".join(board[i]))
    