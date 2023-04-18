import sys
import heapq

INF = 2147000000

input = sys.stdin.readline


def dijkstra(src, sink):
    # 방문 여부 리스트
    chk = [False] * n
    # 비용 리스트 (힙큐 사용을 위해 코스트-인덱스 형태로 저장)
    cost_list = [INF] * n
    cost_list[src] = 0
    # 힙큐 초기화
    hq = []
    heapq.heappush(hq, (0, src))
    # 출발 노드 저장
    path = list(range(n))

    while hq:
        # 현재 최소 비용의 인덱스를 꺼내옴
        start = heapq.heappop(hq)[1]
        # 이미 방문한 노드면 무시하고 다음 순서로
        if chk[start]:
            continue
        for node, cost in graph[start]:
            new_cost = cost_list[start] + cost
            # 최소비용이라면 1. cost_list를 갱신 2. 힙큐에 추가 3. 출발 노드 갱신
            if new_cost < cost_list[node]:
                cost_list[node] = new_cost
                heapq.heappush(hq, (new_cost, node))
                path[node] = start
        # 방문 처리
        chk[start] = True
        # 도착 노드가 방문 처리되었다면 반복 종료
        if chk[sink]:
            break
    return cost_list[sink], path


n = int(input())
m = int(input())
# 단방향 그래프 입력
graph = [[] for _ in range(n)]
for _ in range(m):
    dep, arr, cost = map(int, input().split())
    graph[dep-1].append((arr-1, cost))
src, sink = map(int, input().split())
src -= 1
sink -= 1

# 다익스트라 알고리즘을 수행
min_cost, path = dijkstra(src, sink)

# 최소 비용 출력
print(min_cost)

i = sink
count = 1  # 거쳐간 도시 수
move_reverse = [sink+1]  # 이동 경로 (거꾸로 저장)
while i != src:
    # 현재 노드로 오기위한 출발지를 가져옴
    j = path[i]
    # 거쳐간 도시 개수 추가
    count += 1
    # 경로 추가
    move_reverse.append(j+1)
    # 백트래킹
    i = j
print(count)
print(*move_reverse[::-1])