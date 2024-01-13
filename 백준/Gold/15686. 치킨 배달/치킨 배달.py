import sys
from itertools import combinations

input = sys.stdin.readline
INF = 2147000000

def get_distance(houses, shops):
    total = 0
    for house in houses:
        min_distance = INF
        for shop in shops:
            distance = abs(shop[0] - house[0]) + abs(shop[1] - house[1])
            min_distance = min(min_distance, distance)
        total += min_distance
    return total

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = []
    houses, shops = [], []
    answer = INF
    for i in range(N):
        row = list(map(int, input().split()))
        board.append(row)
        for j in range(N):
            num = row[j]
            if num == 0:
                continue
            elif num == 1:
                houses.append((i, j))
            else:
                shops.append((i, j))
    
    for remains in combinations(shops, M):
        answer = min(answer, get_distance(houses, remains))
        
    print(answer)
