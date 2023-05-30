import sys
from collections import deque

input = sys.stdin.readline
INF = 2147000000


def BFS(start_x, start_y, target_x, target_y):
    que = deque()
    que.append((start_x, start_y, 1))
    visited = [[INF] * N for _ in range(N)]
    visited[start_x][start_y] = 0

    while que:
        x, y, count = que.popleft()
        if x == target_x and y == target_y:
            return count-1
        for nx, ny in ((x-2, y-1), (x-2, y+1), (x, y-2),
                       (x, y+2), (x+2, y-1), (x+2, y+1)):
            if 0 <= nx < N and 0 <= ny < N and count < visited[nx][ny]:
                visited[nx][ny] = count
                que.append((nx, ny, count+1))
    return -1


N = int(input())
start_x, start_y, target_x, target_y = map(int, input().split())

print((BFS(start_x, start_y, target_x, target_y)))