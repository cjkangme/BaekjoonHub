import sys

input = sys.stdin.readline

DX = [-1, 0, 1, 0]
DY = [0, 1, 0, -1]

def dfs(x, y, count):
    global max_count, visited
    
    max_count = max(max_count, count)
    
    for n in range(4):
        xx = x + DX[n]
        yy = y + DY[n]
        if 0<=xx<R and 0<=yy<C:
            new_bit = get_bit(board[xx][yy])
            if not new_bit & visited:
                visited += new_bit
                dfs(xx, yy, count+1)
                visited -= new_bit

def get_bit(char):
    return 1 << (ord(char) - ord("A"))

if __name__ == "__main__":
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    max_count = 0
    visited = get_bit(board[0][0])
   
    dfs(0, 0, 1)
    
    print(max_count)