import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = []
for _ in range(n):
    coins.append(int(input()))

dy = [0] * (k+1)
dy[0] = 1

for coin in coins:
    for i in range(coin, k+1):
        dy[i] += dy[i-coin]

print(dy[-1])