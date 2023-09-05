import sys

input = sys.stdin.readline

def solution(bits, levels):
    total = 0
    min_level, max_level = 2147000000, 0
    for i in range(N):
        if bits & (1 << i):
            total += levels[i]
            min_level = min(min_level, levels[i])
            max_level = max(max_level, levels[i])
    if L <= total <= R and X <= (max_level - min_level):
        return True
    return False
    
    
N, L, R, X = map(int, input().split())
levels = list(map(int, input().split()))
count = 0

for bits in range(2 ** N):
    if solution(bits, levels):
        count += 1

print(count)