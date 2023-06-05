import sys
import heapq

input = sys.stdin.readline

def get_idx(table, d):
    while table[d] != 0:
        d -= 1
    return d

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x : x[1])

hq = []

for p, d in arr:
    heapq.heappush(hq, p)
    if d < len(hq):
        heapq.heappop(hq)

print(sum(hq))