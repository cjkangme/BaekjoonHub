import sys
from collections import defaultdict, deque

input = sys.stdin.readline

def bfs(weight):
    que = deque()
    visited = [False] * (N+1)
    
    que.append(START)
    
    while que:
        node = que.popleft()
        
        if node == TARGET:
            return True
        
        for next_node, max_weight in graph[node].items():
            if not visited[next_node] and weight <= max_weight:
                que.append(next_node)
                visited[next_node] = True
    
    return False

def binary_search(lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        
        # 현재 화물 무게로 목적지 도달 가능
        if bfs(mid):
            lo = mid+1
        # 현재 화물 무게로 목적지 도달 불가
        else:
            hi = mid-1
    
    return hi

if __name__ == "__main__":
    N, M = map(int, input().split())
    # 다리가 여러개일 수 있어 최대값을 저장하기 위해 defaultdict 이용
    graph = [defaultdict(int) for _ in range(N+1)]
    max_weight = 0
    for _ in range(M):
        A, B, C = map(int, input().split())
        # 가장 많이 수송할 수 있는 다리만 저장
        graph[A][B] = max(graph[A][B], C)
        graph[B][A] = max(graph[B][A], C)
        max_weight = max(max_weight, C)
        
    START, TARGET = map(int, input().split())
    
    print(binary_search(1, max_weight))