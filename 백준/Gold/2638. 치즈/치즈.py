import sys
sys.setrecursionlimit(10**6)
from collections import deque


input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def get_outside(x, y):
    for n in range(4):
        xx = x + dx[n]
        yy = y + dy[n]
        # 외부 공기는 -1로 변환
        if 0<=xx<N and 0<=yy<M and not board[xx][yy]:
            board[xx][yy] = -1
            get_outside(xx, yy)
    
N, M = map(int, input().split())
board = []
cheeses = deque()
# 한 줄씩 입력받고, 치즈가 어디있는지를 cheeses 리스트에 저장
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j]:
            cheeses.append((i, j))
    board.append(temp)

# 외부 공간 세기 - 가장 자리는 항상 외부 공기이므로 0,0에서 시작
board[0][0] = -1
get_outside(0, 0)

time = 0
# 치즈가 모두 녹아 없어질때까지 반복
while cheeses:
    # 시간 증가
    time += 1
    # 치즈가 녹은 공간을 저장하는 리스트
    melted = []
    for _ in range(len(cheeses)):
        x, y = cheeses.popleft()
        count = 0
        for n in range(4):
            xx = x + dx[n]
            yy = y + dy[n]
            # 외부공기일 경우 카운트 추가
            if board[xx][yy] == -1:
                count += 1
        # 카운트가 2 미만일 경우 다시 큐에 추가
        if count < 2:
            cheeses.append((x, y))
        else:
            melted.append((x, y))
    # 치즈가 녹은 공간에서 다시 외부 공기 탐색
    for x, y in melted:
        board[x][y] = -1
        get_outside(x, y)
# 정답(시간) 출력
print(time)