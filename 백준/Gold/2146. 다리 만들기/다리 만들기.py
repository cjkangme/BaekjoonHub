import sys
from collections import deque

sys.setrecursionlimit = 100000
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
            
def numbering(i, j, num):
    que = deque()
    que.append((i, j))
    graph[i][j] = num
    while que:
        x, y = que.popleft()
        for n in range(4):
            xx = x + dx[n]
            yy = y + dy[n]
            if 0 <= xx < N and 0 <= yy < N and graph[xx][yy] == 1:
                graph[xx][yy] = num
                que.append((xx, yy))


def BFS(i, j, num):
    global answer
    que = deque()
    que.append((i, j, 1))
    visited[i][j] = 1
    while que:
        x, y, length = que.popleft()
        if length >= answer:
            return answer
        for n in range(4):
            xx = x + dx[n]
            yy = y + dy[n]
            if 0 <= xx < N and 0 <= yy < N and visited[xx][yy] > length + 1:
                if graph[xx][yy] == 0:
                    visited[xx][yy] = length+1
                    que.append((xx, yy, length+1))
                elif graph[xx][yy] != num:
                    return min(length, answer)
    return answer


input = sys.stdin.readline

# input & 변수 초기화
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

MAX_NUM = 2147000000
visited = [[MAX_NUM] * N for _ in range(N)]
answer = MAX_NUM

# 서로 다른 섬 표시 (numbering)
num = 2
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            numbering(i, j, num)
            num += 1

# 다리 탐색 (BFS)
for i in range(N):
    for j in range(N):
        if graph[i][j]:
            for n in range(4):
                ii = i + dx[n]
                jj = j + dy[n]
                if 0 <= ii < N and 0 <= jj < N and not graph[ii][jj] and visited[ii][jj] > 0:
                    answer = BFS(ii, jj, graph[i][j])

print(answer)