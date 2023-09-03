import sys
from itertools import combinations

input = sys.stdin.readline

def solution(sticker_a, sticker_b):
    # a는 90도 회전한 것까지 2가지 경우의 수 따져야 함
    for i in range(2):
        w_a, h_a = sticker_a[i-1], sticker_a[i]
        for j in range(2):
            w_b, h_b = sticker_b[j-1], sticker_b[j]
            if (
                (h_a > H or w_a > W)
                or (h_b > H or w_b > W)
                or ((H - h_b < h_a) and (W - w_b < w_a))
            ):
                continue
            return (h_a * w_a) + (h_b * w_b) # 붙일 수 있으면 붙인 넓이 반환
    return 0 # 붙일 수 없으면 0 반환

if __name__=="__main__":
    H, W = map(int, input().split())
    N = int(input())
    stickers = [list(map(int, input().split())) for _ in range(N)]
    
    max_area = 0
    for combination in combinations(stickers, 2):
        max_area = max(max_area, solution(combination[0], combination[1]))
        
    print(max_area)