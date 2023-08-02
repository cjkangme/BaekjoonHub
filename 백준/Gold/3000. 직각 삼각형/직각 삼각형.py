import sys
from collections import defaultdict

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    answer = 0
    x_dict = defaultdict(int) # 같은 x좌표에 있는 점의 수 저장
    y_dict = defaultdict(int) # 같은 y좌표에 있는 점의 수 저장
    arr = []
    for _ in range(N):
        x, y = map(int, input().split())
        x_dict[x] += 1
        y_dict[y] += 1
        arr.append((x, y))
    # 각 (x, y)가 직각삼각형에서 직각 꼭지점일 때 그릴 수 있는 직각 삼각형 수 계산
    for x, y in arr:
        answer += (x_dict[x]-1) * (y_dict[y]-1) # 자기 자신을 빼야하므로 -1하고 계산
    print(answer)