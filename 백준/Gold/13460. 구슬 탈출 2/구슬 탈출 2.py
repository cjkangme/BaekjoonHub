import sys
from collections import deque, defaultdict

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def move(x, y, d, count):
    xx = x + dx[d]
    yy = y + dy[d]
    if 0 <= xx < N and 0 <= yy < M:
        if board[xx][yy] == 'O':
            return -1, -1, -1, -1
        elif board[xx][yy] != '#':
            return move(xx, yy, d, count+1)
    return x, y, d, count


def BFS(red, blue, move_dict):
    que = deque()
    que.append((red, blue, 0))
    while que:
        r, b, count = que.popleft()
        if count == 10:
            return -1
        for n in range(4):
            rrx, rry, d, r_count = move_dict[r][n]
            bbx, bby, d, b_count = move_dict[b][n]
            if r_count == -1 or b_count == -1:
                if b_count != -1:
                    return count+1
                else:
                    continue
            if rrx == bbx and rry == bby:
                if r_count > b_count:
                    rrx -= dx[d]
                    rry -= dy[d]
                else:
                    bbx -= dx[d]
                    bby -= dy[d]
            que.append(((rrx, rry), (bbx, bby), count+1))
    return -1


N, M = map(int, input().split())
board = [list(map(str, input().rstrip())) for _ in range(N)]
move_dict = defaultdict(list)
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == 'B':
            blue = (i, j)
        if board[i][j] != '#':
            for n in range(4):
                move_dict[(i, j)].append(move(i, j, n, 0))
print(BFS(red, blue, move_dict))