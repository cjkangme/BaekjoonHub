import sys

input = sys.stdin.readline

N = int(input())
times = list(map(int, input().split()))
times.sort()

answer = 0
for i in range(N):
    answer += times[i] * (N-i)
print(answer)