import sys

input = sys.stdin.readline

def reverse(x, y):
    for i in range(3):
        for j in range(3):
            if A[x+i][y+j]:
                A[x+i][y+j] = 0
            else:
                A[x+i][y+j] = 1

N, M = map(int, input().split())
A = [list(map(int, input().rstrip())) for _ in range(N)]
B = [list(map(int, input().rstrip())) for _ in range(N)]
answer = 0
if N >= 3 and M >= 3:
    for i in range(N-2):
        for j in range(M-2):
            if i <= N-3 and j <= M-3:
                if A[i][j] != B[i][j]:
                    reverse(i, j)
                    answer += 1
    if A == B:
        print(answer)
    else:
        print(-1)
else:
    if A == B:
        print(0)
    else:
        print(-1)