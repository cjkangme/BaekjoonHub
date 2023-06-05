import sys
import heapq

input = sys.stdin.readline

def get_idx(table, d):
    while table[d] != 0:
        d -= 1
    return d

n = int(input())
# 오름차순 정렬 (비싼 것부터 나오도록)
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x : x[0])
table = [0] * (n+1)
answer = 0

while arr:
    p, d = arr.pop()
    idx = get_idx(table, min(d, n))
    if idx:
        table[idx] = p
        answer += p
print(answer)