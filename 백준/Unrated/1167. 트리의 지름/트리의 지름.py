import sys
sys.setrecursionlimit(10**6+1)
input = sys.stdin.readline


def DFS(node, total_dist):
    for child, distance in graph[node]:
        if chk[child] > total_dist:
            chk[child] = total_dist+distance
            DFS(child, chk[child])


N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N):
    line = list(map(int, input().split()))

    idx = line[0] - 1
    for i in range(2, len(line), 2):
        child = line[i-1]-1
        distance = line[i]
        graph[idx].append((child, distance))

# 우선 0을 기준으로 가장 먼 노드를 찾는다.
start = 0
chk = [2147000000] * N
chk[start] = 0
DFS(start, 0)

# 0에서 가장 먼 노드를 시작점으로 다시 가장 먼 노드를 찾는다 (지름)
start = chk.index(max(chk))
chk = [2147000000] * N
chk[start] = 0
DFS(start, 0)

print(max(chk))