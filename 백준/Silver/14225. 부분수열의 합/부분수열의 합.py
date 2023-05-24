import sys

input = sys.stdin.readline


def DFS(i, total):
    visited[total] = True
    if i == N:
        return
    DFS(i+1, total+S[i])
    DFS(i+1, total)


N = int(input())
S = list(map(int, input().split()))
visited = [False] * (sum(S)+1)

DFS(0, 0)

try:
    print(visited.index(False))
except ValueError:
    print(sum(S)+1)