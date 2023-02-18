import sys


def check(idx, num):
    answer[idx] = num
    temp = 0
    for i in range(idx, -1, -1):
        temp += answer[i]
        if sign_matrix[i][idx] > 0 and temp <= 0:
            return False
        elif sign_matrix[i][idx] < 0 and temp >= 0:
            return False
        elif sign_matrix[i][idx] == 0 and temp != 0:
            return False
    return True


def DFS(L):
    if L == n:
        print(*answer)
        sys.exit(0)

    else:
        if sign_matrix[L][L] == 0:
            if check(L, 0):
                DFS(L+1)
        else:
            for x in range(1, 11):
                xx = x * sign_matrix[L][L]
                if check(L, xx):
                    DFS(L+1)


if __name__ == "__main__":
    n = int(input())
    S = input()

    sign_matrix = [[None] * n for _ in range(n)]
    answer = [0] * n
    pointer = 0

    for i in range(n):
        for j in range(i, n):
            if S[pointer] == '+':
                sign_matrix[i][j] = 1
            elif S[pointer] == '-':
                sign_matrix[i][j] = -1
            else:
                sign_matrix[i][j] = 0
            pointer += 1

    DFS(0)