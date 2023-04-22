import sys
import heapq
input = sys.stdin.readline

def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
        
    return parents[x]

def union(a, b, parents):
    a = find(a, parents)
    b = find(b, parents)
    # 노드(인덱스)가 작은 정점이 부모가 되도록 함
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

V, E = map(int, input().split())
parents = list(range(V)) # 각 노드의 부모를 저장하는 배열
hq = [] # 최소 힙 (가중치 오름차순)

for _ in range(E):
    A, B, C = map(int, input().split())
    heapq.heappush(hq, (C, A-1, B-1))

answer = 0
count = 1 # V-1개 연결하면 while문 종료하기 위한 변수
while hq:
    cost, a, b = heapq.heappop(hq)
    # 서로의 부모가 다르면(서로소 집합이면) 부모 합치고 count 증가
    if find(a, parents) != find(b, parents):
        union(a, b, parents)
        answer += cost
        count += 1
    if count == V:
        break
        
print(answer)