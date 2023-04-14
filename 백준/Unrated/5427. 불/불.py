import sys
from collections import deque
input = sys.stdin.readline

INF = 2147000000

T = int(input())
DX = [-1, 0, 1, 0]
DY = [0, 1, 0, -1]


def BFS(start, board):
    que = deque()
    # 이동하려는
    que.append((start[0], start[1], 1))
    while que:
        x, y, count = que.popleft()
        for n in range(4):
            xx = x + DX[n]
            yy = y + DY[n]
            if 0 <= xx < h and 0 <= yy < w:
                # 이동할 수 있는 경우
                if count < board[xx][yy]:
                    board[xx][yy] = count
                    que.append((xx, yy, count+1))
            # 인덱스를 벗어난 경우는 탈출한 것
            else:
                return count
    return 'IMPOSSIBLE'


for _ in range(T):
    w, h = map(int, input().split())
    board = [[INF] * w for _ in range(h)]
    fires = []

    # 빌딩 입력받기
    for i in range(h):
        temp = input().rstrip()
        for j in range(w):
            if temp[j] == '.':
                continue
            if temp[j] == '#':
                board[i][j] = -1
            elif temp[j] == '*':
                board[i][j] = 0
                fires.append((i, j))
            else:
                board[i][j] = -1
                start = (i, j)
    # 불이 번지는 시간을 보드에 기록
    for i, j in fires:
        que = deque()
        que.append((i, j, 1))
        while que:
            x, y, count = que.popleft()
            for n in range(4):
                xx = x + DX[n]
                yy = y + DY[n]
                # 이미 다른 곳에서 옮겨붙는 불이 있으면 탐색 X
                if 0 <= xx < h and 0 <= yy < w and count < board[xx][yy]:
                    board[xx][yy] = count
                    que.append((xx, yy, count+1))
    # 사람 탐색
    print(BFS(start, board))