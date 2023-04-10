import sys
from copy import deepcopy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def BFS(board, count):
    board_temp = deepcopy(board)
    que = deque()
    for i, j in viruses:
        que.append((i, j))
        while que:
            x, y = que.popleft()
            for n in range(4):
                xx = x + dx[n]
                yy = y + dy[n]
                if 0<=xx<N and 0<=yy<M and not board_temp[xx][yy]:
                    board_temp[xx][yy] = 2
                    count -= 1
                    que.append((xx, yy))
    return count

N, M = map(int, input().split())
board = []
viruses = []
empty = []
safe_area = 0
answer = 0
for i in range(N):
    temp = list(map(int, input().split()))
    board.append(temp)
    for j in range(M):
        if temp[j] == 0:
            empty.append((i, j))
            safe_area += 1
        elif temp[j] == 2:
            viruses.append((i, j))

visited = [[False]*M for _ in range(N)]            

for a, b, c in combinations(empty, 3):
    board[a[0]][a[1]] = 1
    board[b[0]][b[1]] = 1
    board[c[0]][c[1]] = 1
    answer = max(answer,BFS(board, safe_area-3))
    board[a[0]][a[1]] = 0
    board[b[0]][b[1]] = 0
    board[c[0]][c[1]] = 0

print(answer)