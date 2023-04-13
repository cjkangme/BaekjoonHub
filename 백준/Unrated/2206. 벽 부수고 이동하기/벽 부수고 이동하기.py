import sys
from collections import deque
input = sys.stdin.readline


def BFS():
    DX = [-1, 0, 1, 0]
    DY = [0, 1, 0, -1]

    # 0번 인덱스 : 벽을 안부순 상태에서 방문, 1번 인덱스 : 벽을 부순 상태에서 방문
    visited = [[[False, False] for _ in range(M)] for _ in range(N)]
    que = deque()

    visited[0][0][0] = True
    visited[0][0][1] = True
    que.append((1, 0, 0, 0))

    while que:
        dist, x, y, flag = que.popleft()
        for n in range(4):
            xx = x + DX[n]
            yy = y + DY[n]
            if 0 <= xx < N and 0 <= yy < M:
                if xx == N-1 and yy == M-1:
                    return dist + 1
                if not flag and board[xx][yy] and not visited[xx][yy][1]:
                    visited[xx][yy][1] = True
                    que.append((dist+1, xx, yy, 1))
                if not visited[xx][yy][flag] and not board[xx][yy]:
                    visited[xx][yy][flag] = True
                    que.append((dist+1, xx, yy, flag))
    return -1


N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]

if N == 1 and M == 1:
    answer = 1
else:
    answer = BFS()

print(answer)