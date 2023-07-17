import sys, heapq

input = sys.stdin.readline
INF = 2147000000

# 각 출발도시별 최단경로 찾는 다익스트라 알고리즘
def dijkstra(start):
    costs = [INF] * (n+1)
    costs[start] = 0
    check = [False] * (n+1) # 방문체크가 완료된 노드 저장
    hq = [] # 비용을 우선순위로하는 우선순위 힙큐
    heapq.heappush(hq, (0, start))
    
    while hq:
        cur_cost, node = heapq.heappop(hq)
        # 이미 방문처리 끝난 노드라면 스킵
        if check[node]:
            continue
        # 다익스트라 처리
        for next_node, cost in graph[node].items():
            next_cost = cur_cost + cost
            if next_cost < costs[next_node]:
                costs[next_node] = next_cost
                heapq.heappush(hq, (next_cost, next_node))
        # 방문 처리
        check[node] = True
        
    # 방문할 수 없는 도시를 0으로 바꾸어 저장
    costs = list(map(lambda x: 0 if x == INF else x, costs))
    # 답 출력
    print(*costs[1:])

if __name__=="__main__":
    n = int(input())
    m = int(input())
    
    # 그래프 입력
    graph = [dict() for _ in range(n+1)]
    for _ in range(m):
        start, end, cost = map(int, input().split())
        # 같은 길이 여러번일 수 있으므로 최단경로만 저장하도록 딕셔너리 이용
        try:
            graph[start][end] = min(graph[start][end], cost)
        except KeyError:
            graph[start][end] = cost

    # 각 도시별로 다익스트라 알고리즘 수행
    for i in range(1, n+1):
        dijkstra(i)