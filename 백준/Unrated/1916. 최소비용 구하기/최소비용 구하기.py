import sys
input = sys.stdin.readline

INF = 2147000000


def djikstra(src, tgt):
    # 방문 저장 배열, 거리 저장 배열
    visited = [False] * N
    distance = [INF] * N
    distance[src] = 0  # 시작을 위해 최대값보다 1작게

    while True:
        # 모든 노드를 방문해 start를 갱신할 수 없을 때(-1) 빠져 나옴
        start = -1
        min_dist = INF
        for i in range(N):
            if not visited[i] and distance[i] < min_dist:
                min_dist = distance[i]
                start = i
        # 빠져나올때 답 반환
        if visited[tgt]:
            return distance[tgt]
        # distance 갱신
        for node, dist in graph[start]:
            distance[node] = min(distance[node], distance[start] + dist)
        # 방문처리
        visited[start] = True


N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b, dist = map(int, input().split())
    graph[a-1].append((b-1, dist))
src, tgt = map(lambda x: x-1, map(int, input().split()))

answer = djikstra(src, tgt)

print(answer)