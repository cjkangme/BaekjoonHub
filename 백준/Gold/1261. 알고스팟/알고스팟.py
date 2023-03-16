import sys
from collections import deque
input = sys.stdin.readline

def BFS(end_x, end_y, maze):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    que = deque()
    que.append((0, 0, 0))
    temp_que = []
    
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    
    while True:
        x, y, cnt = que.popleft()
        
        if x == end_x and y == end_y:
            return cnt
        
        for n in range(4):
            xx = x + dx[n]
            yy = y + dy[n]
            
            if 0<=xx<N and 0<=yy<M and not visited[xx][yy]:
                if maze[xx][yy] == 0:
                    que.append((xx, yy, cnt))
                    visited[xx][yy] = True
                else:
                    temp_que.append((xx, yy, cnt+1))
                    visited[xx][yy] = True
                    
        if not que:
            que.extend(temp_que)
            temp_que = []

M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]

print(BFS(N-1, M-1, maze))