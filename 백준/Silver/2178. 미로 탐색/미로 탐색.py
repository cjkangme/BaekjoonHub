from collections import deque
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(board):
    que = deque()
    que.append((0, 0, 1))
    
    while que:
        x, y, count = que.popleft()
        if x == N-1 and y == M-1:
            return count
        for i in range(4):
            xx = x+dx[i]
            yy = y+dy[i]
            if 0<=xx<N and 0<=yy<M and board[xx][yy] == 1:
                board[xx][yy] = 0
                que.append((xx, yy, count+1))

if __name__=="__main__":
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int,input().rstrip())))
    
    board[0][0] = 0
    answer = BFS(board)
    
    print(answer)