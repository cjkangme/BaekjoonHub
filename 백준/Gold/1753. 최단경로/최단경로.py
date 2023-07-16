import sys, heapq

input = sys.stdin.readline
INF = 2147000000

def djikstra(start):
    check = [False] * (V+1) # 방문 노드 체크
    costs = [INF] * (V+1) # start에서 i번 노드까지 가기 위하 최소비용 저장
    costs[start] = 0
    hq = [] # 다음에 방문할 노드 저장하는 최소힙
    heapq.heappush(hq, (0, start))
    
    while hq:
        cost, node = heapq.heappop(hq)
        
        # 이미 방문 종료된 노드라면 건너뛰기
        if check[node]:
            continue
        for next_node, weight in graph[node].items():
            next_cost = cost + weight
            # 방문할 수 있는 경로가 최단 경로라면 갱신 및 방문 리스트 추가
            if next_cost < costs[next_node]:
                costs[next_node] = next_cost
                heapq.heappush(hq, (next_cost, next_node))
        
        # 방문 완료 처리
        check[node] = True
    
    # 0번인덱스는 버리므로 1번 인덱스부터 반환
    return costs[1:]

if __name__=="__main__":
    V, E = map(int, input().split())
    start = int(input())
    graph = [dict() for _ in range(V+1)]
    
    # 간선 입력받아 그래프에 저장
    for _ in range(E):
        u, v, w = map(int, input().split())
        # 간선이 여러개일 수 있으므로, 딕셔너리 이용해 최소값 저장
        try:
            graph[u][v] = min(graph[u][v], w)
        except KeyError:
            graph[u][v] = w
    
    for answer in djikstra(start):
        print(answer if answer != INF else "INF")