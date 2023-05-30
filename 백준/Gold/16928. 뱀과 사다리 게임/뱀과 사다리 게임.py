import sys
from collections import deque

input = sys.stdin.readline
INF = 2147000000

def BFS(warps):
    que = deque()
    que.append((1, 1))
    visited = [INF] * 101
    visited[1] = 0
    
    while que:
        point, count = que.popleft()
        for i in range(1, 7):
            if warps.get(point+i) is not None:
                next_point = warps[point+i]
            else:
                next_point = point+i
            if next_point > 100:
                continue
            elif next_point == 100:
                return count
            else:
                if count < visited[next_point]:
                    visited[next_point] = count
                    que.append((next_point, count+1))

N, M = map(int, input().split())
warps = dict()
for _ in range(N+M):
    start, end = map(int, input().split())
    warps[start] = end

print(BFS(warps))