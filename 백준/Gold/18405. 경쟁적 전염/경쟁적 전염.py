import sys
from collections import deque

input = sys.stdin.readline
INF = 2147000000

def BFS():
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    que = deque()
    # 바이러스에 있는 것을 낮은 순서 번호로 큐에 추가
    for _, i, j in viruses:
        que.append((i, j, 1))
    
    while que:
        x, y, count = que.popleft()
        
        if count > S:
            break
        
        for n in range(4):
            xx = x + dx[n]
            yy = y + dy[n]
            
            if 0<=xx<N and 0<=yy<N and count < board[xx][yy][0]:
                board[xx][yy][0] = count
                board[xx][yy][1] = board[x][y][1]
                que.append((xx, yy, count+1))
            
if __name__ == "__main__":
    N, K = map(int, input().split())
    board = [[] for _ in range(N)]
    viruses = []
    # BFS 탐색할 보드 입력, BFS 탐색 위해 카운트 변수 추가
    for i in range(N):
        row = list(map(int, input().split()))
        for j, num in enumerate(row):
            # 바이러스가 있는 칸이면 시작점으로 세팅, 아니면 INF로
            if num > 0:
                board[i].append([0, num])
                viruses.append((num, i, j))
            else:
                board[i].append([INF, 0])
    # 낮은 순서부터 탐색해야 하므로 바이러스 리스트를 오름차순 정렬
    viruses.sort(key=lambda x : x[0])
    S, X, Y = map(int, input().split())
    
    BFS()
    print(board[X-1][Y-1][1])