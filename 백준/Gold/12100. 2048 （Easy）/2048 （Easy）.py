import sys
from copy import deepcopy


def move(x, y, dx, dy, board):
    xx = x + dx
    yy = y + dy
    while True:
        if 0 <= xx < N and 0 <= yy < N:
            if not board[xx][yy]:
                xx += dx
                yy += dy
                continue
            else:
                if board[x][y] == board[xx][yy]:
                    board[x][y] *= -2
                    break
                else:
                    xx -= dx
                    yy -= dy
                    break
        else:
            xx -= dx
            yy -= dy
            break
    if x != xx or y != yy:
        board[xx][yy] = board[x][y]
        board[x][y] = 0
    return board


def up(board):
    for j in range(N):
        for i in range(1, N):
            if board[i][j]:
                board = move(i, j, -1, 0, board)
        for i in range(N):
            board[i][j] = abs(board[i][j])
    return board


def right(board):
    for i in range(N):
        for j in range(N-2, -1, -1):
            if board[i][j]:
                board = move(i, j, 0, 1, board)
        for j in range(N):
            board[i][j] = abs(board[i][j])
    return board


def down(board):
    for j in range(N):
        for i in range(N-2, -1, -1):
            if board[i][j]:
                board = move(i, j, 1, 0, board)
        for i in range(N):
            board[i][j] = abs(board[i][j])
    return board


def left(board):
    for i in range(N):
        for j in range(1, N):
            if board[i][j]:
                board = move(i, j, 0, -1, board)
        for j in range(N):
            board[i][j] = abs(board[i][j])
    return board


def DFS(L, board):
    global answer
    if L == 5:
        answer = max(answer, max(map(max, board)))
        return
    else:
        DFS(L+1, up(deepcopy(board)))
        DFS(L+1, right(deepcopy(board)))
        DFS(L+1, down(deepcopy(board)))
        DFS(L+1, left(deepcopy(board)))


input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N = int(input())
init_board = [list(map(int, input().split())) for _ in range(N)]
if N > 1:
    answer = 0
    DFS(0, init_board)
else:
    answer = init_board[0][0]
print(answer)