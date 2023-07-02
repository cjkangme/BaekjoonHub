import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global house_count
    board[x][y] = 0
    house_count += 1
    for k in range(4):
        xx = x+dx[k]
        yy = y+dy[k]
        if 0 <= xx < N and 0 <= yy < N and board[xx][yy] == 1:
            DFS(xx, yy)


if __name__ == "__main__":
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().rstrip())))

    count = 0
    house = []

    for i in range(N):
        for j in range(N):
            house_count = 0
            if board[i][j] == 1:
                DFS(i, j)
                count += 1
                house.append(house_count)

    house.sort()
    print(count)
    for cnt in house:
        print(cnt)
