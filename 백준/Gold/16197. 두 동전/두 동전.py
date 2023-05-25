import sys
from collections import deque

input = sys.stdin.readline

def BFS(coins):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    que = deque()
    que.append((coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0))
    while que:
        x1, y1, x2, y2, count = que.popleft()
        if count == 10:
            return -1
        for n in range(4):
            xx1 = x1 + dx[n]
            yy1 = y1 + dy[n]
            xx2 = x2 + dx[n]
            yy2 = y2 + dy[n]
            nx1, ny1, nx2, ny2 = x1, y1, x2, y2
            if 0<=xx1<N and 0<=yy1<M and 0<=xx2<N and 0<=yy2<M:
                if board[xx1][yy1] != '#':
                    nx1, ny1 = xx1, yy1
                if board[xx2][yy2] != '#':
                    nx2, ny2 = xx2, yy2
                # 겹치면 안됨
                if nx1 != nx2 or ny1 != ny2:
                    que.append((nx1, ny1, nx2, ny2, count+1))
            else:
                # 둘 중 하나는 안에 남아있어야 함
                if (0<=xx1<N and 0<=yy1<M) or (0<=xx2<N and 0<=yy2<M):
                    return count + 1
    return -1


N, M = map(int, input().split())
board = []
coins = []
for i in range(N):
    temp = list(map(str, input().rstrip()))
    for j in range(M):
        if temp[j] == 'o':
            coins.append((i, j))
    board.append(temp)

print(BFS(coins))