import sys
sys.setrecursionlimit(10 ** 6)

input = sys.stdin.readline
DX = [-1, 0, 1, 0]
DY = [0, 1, 0, -1]

def normal_dfs(x, y, color, visited):
    for n in range(4):
        xx = x + DX[n]
        yy = y + DY[n]
        if (0<=xx<N and 0<=yy<N
        and board[xx][yy] == color 
        and not visited[xx][yy]):
            visited[xx][yy] = True
            normal_dfs(xx, yy, color, visited)
            
def weak_dfs(x, y, color, visited):
    for n in range(4):
        xx = x + DX[n]
        yy = y + DY[n]
        if 0<=xx<N and 0<=yy<N:
            flag = False
            if color == "B":
                if board[xx][yy] == "B":
                    flag = True
            else:
                if board[xx][yy] == "R" or board[xx][yy] == "G":
                    flag = True
            if flag and not visited[xx][yy]:
                visited[xx][yy] = True
                weak_dfs(xx, yy, color, visited)

if __name__ == "__main__":
    N = int(input())
    board = [list(map(str, input().rstrip())) for _ in range(N)]
    
    normal_count, weak_count = 0, 0
    
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                normal_dfs(i, j, board[i][j], visited)
                normal_count += 1
                
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                weak_dfs(i, j, board[i][j], visited)
                weak_count += 1
    print(normal_count, weak_count)