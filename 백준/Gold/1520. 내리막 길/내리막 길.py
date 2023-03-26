import sys
sys.setrecursionlimit(500*500)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
board = dict()
dt = [[0] * N for _ in range(M)]
dt[0][0] = 1
for i in range(M):
    arr = list(map(int, input().split()))
    for j, height in enumerate(arr):
        board[(i, j)] = height

# 가장 높은 높이부터 처리
sorted_d = dict(sorted(board.items(), key=lambda x : x[1], reverse=True))
for coord, height in sorted_d.items():
    x, y = coord
    for n in range(4):
        xx = x + dx[n]
        yy = y + dy[n]
        if 0<=xx<M and 0<=yy<N and height < board[(xx, yy)]:
            dt[x][y] += dt[xx][yy]

print(dt[-1][-1])