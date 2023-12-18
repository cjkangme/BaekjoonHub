import sys
from collections import deque

input = sys.stdin.readline

def BFS(board, que, count, max_count):
    dx = [-1, 0, 1, 0, 0, 0]
    dy = [0, 1, 0, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    
    while que and count < max_count:
        x, y, z, day = que.popleft()
        for n in range(6):
            xx = x + dx[n]
            yy = y + dy[n]
            zz = z + dz[n]
            if (0<=xx<N and 0<=yy<M and 0<=zz<H and board[zz][xx][yy] == 0):
                board[zz][xx][yy] = 1
                que.append((xx, yy, zz, day+1))
                count += 1
    
    if count == max_count:
        return day
    return -1

if __name__ == "__main__":
    M, N, H = map(int, input().split())
    max_count = M * N * H
    count = 0
    board = [[] for _ in range(H)]
    que = deque()
    for k in range(H):
        for i in range(N):
            row = list(map(int, input().split()))
        
            board[k].append(row)
            for j in range(M):
                if row[j] == 1:
                    que.append((i, j, k, 1))
                    count += 1
                elif row[j] == -1:
                    max_count -= 1
    if (count == max_count):
        print(0)
    else:
        print(BFS(board, que, count, max_count))