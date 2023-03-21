import sys
from collections import deque
input = sys.stdin.readline


def find_eertree(i, j, array):
    que = deque()
    que.append((i, j))
    eertree.add((i, j))

    while que:
        left, right = que.popleft()
        eertree.add((left, right))
        ll, rr = left-1, right+1
        if ll >= 0 and rr < N and array[ll] == array[rr]:
            que.append((ll, rr))


N = int(input())
array = list(map(int, input().split()))
eertree = set()
for i in range(N):
    find_eertree(i, i, array)
    if i+1 < N and array[i] == array[i+1]:
        find_eertree(i, i+1, array)
M = int(input())
for _ in range(M):
    S, E = map(int, input().split())
    print(1 if (S-1, E-1) in eertree else 0)