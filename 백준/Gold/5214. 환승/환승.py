import sys
from collections import deque

input = sys.stdin.readline
INF = 2147000000

def bfs():
    que = deque()
    que.append((1, 2))
    visited = [False] * M
    
    while que:
        station, count = que.popleft()
        for idx in idx_set[station]:
            if not visited[idx]:
                visited[idx] = True
                for next_station in hypertubes[idx]:
                    if count < distance[next_station]:
                        distance[next_station] = count
                        que.append((next_station, count+1))

if __name__ == "__main__":
    N, K, M = map(int, input().split())
    distance = [INF] * (N+1) # 1번 역부터의 거리
    distance[1] = 1
    idx_set = [[] for _ in range(N+1)]
    
    hypertubes = []
    for i in range(M):
        hypertube = list(map(int, input().split()))
        for tube in hypertube:
            idx_set[tube].append(i)
        hypertubes.append(hypertube)
    
    bfs()
    
    print(distance[N] if distance[N] != INF else -1)