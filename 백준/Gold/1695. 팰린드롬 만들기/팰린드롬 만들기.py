import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

dp = [[0] * N for _ in range(2)]

for i in reversed(range(N)):
    for j in range(i+1, N):
        row = i % 2
        if arr[i] == arr[j]:
            dp[row][j] = dp[row-1][j-1]
        else:
            dp[row][j] = min(dp[row][j-1], dp[row-1][j]) + 1

print(dp[0][-1])