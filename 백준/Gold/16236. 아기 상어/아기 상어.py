import sys
from collections import deque

input = sys.stdin.readline

def BFS(i, j, size):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    que = deque()
    visited = [[False] * N for _ in range(N)]
    que.append((i, j, 1))
    visited[i][j] = True
    return_list = []
    flag = 2147000000
    while que:
        x, y, count = que.popleft()
        if count > flag:
            break
        for n in range(4):
            xx = x + dx[n]
            yy = y + dy[n]
            if 0<=xx<N and 0<=yy<N and not visited[xx][yy]:
                if not board[xx][yy]:
                    que.append((xx, yy, count+1))
                    visited[xx][yy] = True
                elif board[xx][yy] > size:
                    continue
                elif board[xx][yy] < size:
                    visited[xx][yy] = True
                    return_list.append((xx, yy, count))
                    flag = count
                else:
                    que.append((xx, yy, count+1))
                    visited[xx][yy] = True
    if return_list:
        return_list.sort(key=lambda x: (x[0], x[1]))
        return return_list[0]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
size = 2
count = 0
answer = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            x, y = i, j
            board[i][j] = 0

while True:
    result = BFS(x, y, size)
    if result:
        x, y, temp = result
        board[x][y] = 0
        answer += temp
        count += 1
        if count == size:
            count = 0
            size += 1
    else:
        break
        
print(answer) 