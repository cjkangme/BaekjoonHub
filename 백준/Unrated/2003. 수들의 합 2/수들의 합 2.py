import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
total = 0
answer = 0
right = 0

for left in range(N):
    right = max(left, right)

    while total < M and right < N:
        total += A[right]
        right += 1

    if total == M:
        answer += 1

    total -= A[left]

print(answer)