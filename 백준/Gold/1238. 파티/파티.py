import sys, heapq
from collections import deque

input = sys.stdin.readline
INF = 2147000000

def dijkstra(start):
    costs = [INF] * (N+1)
    visited = [False] * (N+1)
    costs[start] = 0
    node = start
    hq = []
    
    while True:
        for next_node, cost in graph[node]:
            next_cost = costs[node] + cost
            if not visited[next_node] and costs[next_node] > next_cost:
                costs[next_node] = next_cost
                heapq.heappush(hq, (next_cost, next_node))
        visited[node] = True
        
        if hq:
            _, node = heapq.heappop(hq)
        else:
            break
    
    return costs

if __name__=="__main__":
    N, M, X = map(int, input().split())
    # 단방향 그래프 입력
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end, time = map(int, input().split())
        graph[start].append((end, time))
    answer = [0] * (N+1)
    for node in range(1, N+1):
        if node == X:
            costs = dijkstra(node)
            for idx, val in enumerate(costs):
                answer[idx] += val
        else:
            answer[node] += dijkstra(node)[X]
    print(max(answer[1:]))