import sys
input = sys.stdin.readline

N, K = map(int, input().split())
dp = {0:0}

for _ in range(N):
    w, v = map(int, input().split())
    temp = dict()
    for value, weight in dp.items():
        ww = w + weight
        vv = v + value
        if ww < dp.get(vv, K+1):
            temp[vv] = ww
    dp.update(temp)
    
print(max(dp.keys()))