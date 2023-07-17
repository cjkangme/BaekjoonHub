import sys

input = sys.stdin.readline
INF = 2147000000

# 벨만포드 알고리즘
def bellman_ford(start):
    costs = [INF] * (N+1)
    costs[start] = 0
    # N-1 번 수행
    for _ in range(N-1):
        # 모든 간선을 탐색
        for key, cost in edges.items():
            s, e = key
            # 한번 이상 계산된 간선에 대해서만 간선 탐색
            if costs[s] != INF:
                next_cost = costs[s] + cost
                if next_cost < costs[e]:
                    costs[e] = next_cost
    if costs[start] < 0:
        return True
    else:
        return False
    
if __name__=="__main__":
    TC = int(input())
    for _ in range(TC):
        N, M, W = map(int, input().split())
        
        edges = dict() 
        # 벨만 포드 알고리즘을 위해 모든 간선을 리스트에 추가
        for _ in range(M):
            S, E, T = map(int, input().split())
            try:
                edges[(S, E)] = min(edges[(S, E)], T)
            except KeyError:
                edges[(S, E)] = T
            try:
                edges[(E, S)] = min(edges[(E, S)], T)
            except KeyError:
                edges[(E, S)] = T
        candidates = []
        for _ in range(W):
            S, E, T = map(int, input().split())
            candidates.append(E)
            edges[(S, E)] = -T
        
        # 모든 노드에 대해 벨만포드 알고리즘을 돌려서 시간 여행이 되면 YES 출력
        for candidate in candidates:
            if bellman_ford(candidate):
                print("YES")
                break
        # 모든 노드에 대해 탐색해도 시간 여행 안되면 NO 출력
        else:
            print("NO")