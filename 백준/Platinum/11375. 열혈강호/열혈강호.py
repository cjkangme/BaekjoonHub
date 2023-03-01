import sys
input = sys.stdin.readline

def DFS(node):
    if visited[node]:
        return False
    visited[node] = True
    
    for work in graph[node]:
        if match[work] == -1 or DFS(match[work]):
            match[work] = node
            return True
    return False
    

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
match = [-1 for _ in range(M+1)]

answer = 0

for i in range(N):
    works = list(map(int, input().split()))
    graph[i] = works[1:]
for i in range(N):
    visited = [False for _ in range(N)]
    if DFS(i):
        answer += 1
print(answer)