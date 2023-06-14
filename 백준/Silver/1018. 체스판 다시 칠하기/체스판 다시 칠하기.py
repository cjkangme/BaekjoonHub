import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(N)]

answer = 2147000000
white_list = [] # 0,0 칸을 흰색으로 칠할 경우 새로 칠해야하는 칸
black_list = [] # 0,0 칸을 검정색으로 할 경우 새로 칠해야하는 칸

for i in range(N):
    for j in range(M):
        # 둘 중 하나만 홀수인 경우
        if (i+j) % 2:
            if board[i][j] == "W":
                white_list.append((i, j))
            else:
                black_list.append((i, j))
        # 둘 다 짝수거나 둘 다 홀수인 경우
        else:
            if board[i][j] == "W":
                black_list.append((i, j))
            else:
                white_list.append((i, j))

for i in range(N-7):
    for j in range(M-7):
        white_count = 0
        black_count = 0
        for x, y in white_list:
            if i <= x <= i+7 and j <= y <= j+7:
                white_count += 1
        for x, y in black_list:
            if i <= x <= i+7 and j <= y <= j+7:
                black_count += 1
        answer = min(answer, white_count, black_count)

print(answer)          