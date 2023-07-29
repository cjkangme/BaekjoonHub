import sys
from collections import deque

input = sys.stdin.readline

def BFS(start, target):
    que = deque()
    que.append((start, 0))
    visited = [False] * N
    visited[start] = True
    
    while que:
        node, curr_distance = que.popleft()
        if node == target:
            break
        
        for next_node, next_distance in tree[node]:
            if not visited[next_node]:
                temp = curr_distance + next_distance
                que.append((next_node, temp))
                distances[start][next_node] = temp
                distances[next_node][start] = temp
                visited[next_node] = True

    return

if __name__ == "__main__":
    N, M = map(int, input().split())
    tree = [[] for _ in range(N)]
    distances = [[0] * N for _ in range(N)]

    for _ in range(N-1):
        a, b, distance = map(int, input().split())
        tree[a-1].append((b-1, distance))
        tree[b-1].append((a-1, distance))

    for _ in range(M):
        a, b = map(int, input().split())
        if not distances[a-1][b-1]:
            BFS(a-1, b-1)

        print(distances[a-1][b-1])