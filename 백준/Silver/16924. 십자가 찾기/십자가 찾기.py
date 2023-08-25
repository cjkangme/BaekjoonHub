import sys

input = sys.stdin.readline
DX = [-1, 0, 1, 0]
DY = [0, 1, 0, -1]

def draw_cross(x, y):
    flag = False
    drawed_count = -1
    is_drawed = drawed[x][y]
    temp = [[x, y] for _ in range(4)]
    while True:
        drawed_count += 1
        for i in range(4):
            drawed[temp[i][0]][temp[i][1]] = True
            xx, yy = temp[i][0] + DX[i], temp[i][1] + DY[i]
            if 0<=xx<N and 0<=yy<M and board[xx][yy] == "*":
                temp[i] = [xx, yy]
            else:
                flag = True
        if flag:
            if drawed_count == 0 and not is_drawed:
                drawed[x][y] = False
            return drawed_count
        

if __name__=="__main__":
    N, M = map(int, input().split())
    board = [list(map(str, input().rstrip())) for _ in range(N)]
    crosses = []
    draw_points = []
    drawed = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == "*":
                crosses.append((i, j))
                drawed_count = draw_cross(i, j)
                if drawed_count:
                    draw_points.append((i+1, j+1, drawed_count))
                    
    for x, y in crosses:
        if not drawed[x][y]:
            print(-1)
            sys.exit(0)
    
    print(len(draw_points))
    [print(i, j, s) for i, j, s in draw_points]