# 현재 칸에 퀸을 놓을 수 있는지 판별하는 함수
# x: 판별할 칸의 행 좌표
def is_queen(x):
    # 이전 행에 놓였던 퀸에 대해 탐색
    for xx in range(x):
        # 이전 행에 놓인 퀸과 같은 열이거나, 대각선에 있을 경우 놓을 수 없음
        if board[x] == board[xx] or abs(board[x]-board[xx]) == abs(x-xx):
            return False
    return True
    
# 퀸을 놓을 수 있는 칸에 퀸을 놓는 함수
# i: 현재 보드에 놓인 퀸의 개수(이번에 놓아야할 퀸의 행 번호)
def put_queen(i):
    global answer
    # 보드에 퀸이 N개만큼 놓이면 방법의 수를 1증가 시킴
    if i == N:
        answer += 1
        return

    for j in range(N):
        board[i] = j
        if is_queen(i):
            put_queen(i+1)

if __name__=="__main__":
    N = int(input())
    answer = 0
    # 배열 초기화
    board = [-1] * N
    
    # 무조건 한 줄에 하나씩 있을 수 있으므로 각 줄을 탐색하면 됨
    put_queen(0)
    
    print(answer)