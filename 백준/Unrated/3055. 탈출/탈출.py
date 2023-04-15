import sys
from collections import deque

input = sys.stdin.readline
INF = 2147000000


def flood(waters, dx, dy):
    temp = []
    for i, j in waters:
        for n in range(4):
            ii = i+dx[n]
            jj = j+dy[n]
            # 고슴도치가 지나온 길도 물이 들어올 수 있음
            if 0 <= ii < R and 0 <= jj < C and board[ii][jj]:
                temp.append((ii, jj))
                board[ii][jj] = 0
    return temp


def BFS(start, board, waters):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for i, j in waters:
        que = deque()
        que.append((i, j, 1))
        board[i][j] = 0
        while que:
            x, y, count = que.popleft()
            for n in range(4):
                xx = x+dx[n]
                yy = y+dy[n]
                if 0 <= xx < R and 0 <= yy < C and count < board[xx][yy]:
                    board[xx][yy] = count
                    que.append((xx, yy, count+1))

    que = deque()
    que.append((start[0], start[1], 1))
    while que:
        x, y, count = que.popleft()
        for n in range(4):
            xx = x+dx[n]
            yy = y+dy[n]
            if 0 <= xx < R and 0 <= yy < C:
                if xx == N and yy == M:
                    return count
                # 물이 들어찰 예정지는 갈 수 없음
                if count < board[xx][yy]:
                    board[xx][yy] = count
                    que.append((xx, yy, count+1))
    return 'KAKTUS'


R, C = map(int, input().split())

board = [[INF] * C for _ in range(R)]
waters = []
# 입력받기
for i in range(R):
    temp = list(input().rstrip())
    for j in range(C):
        if temp[j] == '.':
            continue
        elif temp[j] == 'X':
            board[i][j] = -1
        elif temp[j] == '*':
            board[i][j] = 0
            waters.append((i, j))
        elif temp[j] == 'D':
            board[i][j] = -1
            N, M = i, j
        else:
            start = (i, j)

print(BFS(start, board, waters))