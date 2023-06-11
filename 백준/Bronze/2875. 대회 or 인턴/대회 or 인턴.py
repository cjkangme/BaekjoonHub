from math import ceil

N, M, K = map(int, input().split())

total = N + M
team = min(N//2, M)
remain = total - team * 3

if remain < K:
    team -= ceil((K-remain) / 3)
    
print(max(0, team))