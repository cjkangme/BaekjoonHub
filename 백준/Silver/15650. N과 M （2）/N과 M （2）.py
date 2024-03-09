def DFS(L, n, arr):
    if L == M:
        print(*arr)
        return
    for nn in range(n+1, N+1):
        DFS(L+1, nn, arr + [nn])

if __name__=="__main__":
    N, M = map(int, input().split())
    for i in range(1, N-M+2):
        DFS(1, i, [i])
