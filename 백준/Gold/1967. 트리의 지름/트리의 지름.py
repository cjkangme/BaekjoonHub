import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def DFS(node, dist):
    chk[node] = dist
    for link, weight in tree[node]:
        if chk[link] > dist:
            DFS(link, dist+weight)


N = int(input())
tree = [[] for _ in range(N)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    a, b = a-1, b-1
    tree[a].append((b, w))
    tree[b].append((a, w))

INF = 2147000000
# 임의의 노드 하나에서 최대 거리를 갖는 노드 탐색 -> 한쪽 끝
chk = [INF] * N
chk[0] = 0
DFS(0, 0)

# 최대 거리 노드에서 다시 최대 거리를 갖는 노드 탐색 -> 지름
start = chk.index(max(chk))
chk = [INF] * N
chk[start] = 0
DFS(start, 0)

print(max(chk))