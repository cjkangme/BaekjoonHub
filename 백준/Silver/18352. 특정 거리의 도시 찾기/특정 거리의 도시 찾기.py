import sys
from collections import deque

input = sys.stdin.readline
INF = 2147000000

# BFS 탐색
def BFS(start):
    que = deque()
    que.append((start, 0))
    costs = [INF] * (N+1)
    costs[start] = 0
    answer = [] # 정답이 담길 배열
    
    while que:
        node, cost = que.popleft()
        
        # 거리가 K를 넘었다면 BFS 특성상 앞으로 K보다 작거나 같은 노드 안나옴
        if cost > K:
            break
        
        for next_node in graph[node]:
            next_cost = cost + 1
            if next_cost < costs[next_node]:
                # 다음에 방문할 노드 최단거리가 K이면 반환할 답에 추가
                if next_cost == K:
                    answer.append(next_node)
                    costs[next_node] = next_cost
                # 아니면 큐에 추가
                else:
                    que.append((next_node, next_cost))
                    costs[next_node] = next_cost
    # 오름차순 정렬 후 반환
    answer.sort()
    return answer

if __name__ == "__main__":
    N, M, K, X = map(int, input().split())
    
    # 그래프 입력
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append(end)
    
    answer = BFS(X)
    if answer:
        [print(a) for a in answer]
    else:
        print(-1)