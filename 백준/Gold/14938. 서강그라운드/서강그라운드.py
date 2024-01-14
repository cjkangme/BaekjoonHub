import sys
from collections import deque

input = sys.stdin.readline
INF = 2147000000

def BFS(start, max_move):
    dq = deque()
    item = item_list[start]
    visited = [INF] * n
    visited[start] = 0
    dq.append((start, 0))
    
    while dq:
        area, moved = dq.popleft()
        for next_area, cost in graph[area]:
            next_move = moved + cost
            if next_move <= max_move and next_move < visited[next_area]:
                if visited[next_area] == INF:
                    item += item_list[next_area]
                visited[next_area] = next_move
                dq.append((next_area, next_move))
    return item

if __name__ == "__main__":
    n, m, r = map(int, input().split())
    answer = 0
    item_list = list(map(int, input().split()))
    graph = [[] for _ in range(n)]
    for _ in range(r):
        a, b, cost = map(int, input().split())
        graph[a-1].append((b-1, cost))
        graph[b-1].append((a-1, cost))

    for i in range(n):
        answer = max(answer, BFS(i, m))
        
    print(answer)
    