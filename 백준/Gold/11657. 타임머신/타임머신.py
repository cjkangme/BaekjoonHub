import sys

INF = 2147000000

N, M = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]
costs = [INF] * (N+1)
costs[1] = 0
flag = False

# 출발지 순으로 정렬
edges.sort()

# 노드의 수 - 1 만큼 반복 + 루프있는지 확인을 위한 마지막 탐색
for i in range(N):
    # 모든 간선에 대해 탐색
    for edge in edges:
        start, end, cost = edge
        # 최소비용 갱신
        if costs[start] != INF and costs[start] + cost < costs[end]:
            costs[end] = costs[start] + cost
            # 마지막 탐색일 경우 무한 순환이므로 플래그
            if i == N-1:
                flag = True
                break
if flag:
    print(-1)
else:
    for i in range(2, N+1):
        print(costs[i] if costs[i] != INF else -1)