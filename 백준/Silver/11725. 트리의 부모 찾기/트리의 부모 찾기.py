import sys
sys.setrecursionlimit(100001)
input = sys.stdin.readline

def DFS(node):
    for i in graph[node]:
        if parents[i] == -1:
            parents[i] = node
            DFS(i)
    
N = int(input())
graph = [[] for _ in range(N)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

parents = [-1] * N
parents[0] = 0
DFS(0)

for i in range(1, N):
    print(parents[i]+1)