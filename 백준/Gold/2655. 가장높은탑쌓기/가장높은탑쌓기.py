import sys

input = sys.stdin.readline
INF = 2147000000

if __name__ == "__main__":
    N = int(input())
    # 밑면 넓이 - 높이 - 무게 순
    bricks = []
    for i in range(N):
        a, h, w = map(int, input().split())
        bricks.append((a, h, w, i+1))
    
    # 밑면 넓이에 대해서 오름차순 정렬
    bricks.sort(key=lambda x : x[0])
    # 다이나믹 테이블 정의 - 현재 높이, 현재 탑에 쌓인 벽돌, 마지막 벽돌의 인덱스
    dt = [bricks[i][1] for i in range(N)]
    
    # DP 구하기
    for i in range(1, N):
        for j in range(i):
            if bricks[j][2] < bricks[i][2]:
                dt[i] = max(dt[i], dt[j]+bricks[i][1])
    # 최대값 인덱스 찾기
    max_h = max(dt)
    idx = dt.index(max_h)
    tower = []
    for i in range(idx, -1, -1):
        if dt[i] == max_h:
            tower.append(bricks[i][3])
            max_h -= bricks[i][1]
            
    print(len(tower))
    [print(idx) for idx in reversed(tower)]