import sys

input = sys.stdin.readline
INF = 2147000000
# d가 0이면 ㄹ자 모양, 1이면 w자 모양
def zigzag(idx, d):
    if d == 0:
        if idx % 2 == 0:
            return ("R" * (C-1))
        else:
            return ("L" * (C-1))
    else:
        if idx % 2 == 0:
            return ("D" * (R-1))
        else:
            return ("U" * (R-1))
    

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
answer = ""
# 행이 홀수인 경우 (행,열 둘다 홀수인 경우 포함)
if R % 2 == 1:
    for i in range(R):
        answer += zigzag(i, 0)
        if i < R-1:
            answer += "D"
# 열이 홀수인 경우
elif C % 2 == 1:
    for i in range(C):
        answer += zigzag(i, 1)
        if i < C-1:
            answer += "R"
# 둘 다 짝수인 경우
else:
    # 피할 칸 구하기
    min_fun = INF
    for i in range(R):
        for j in range(C):
            if (i + j) % 2 and board[i][j] <= min_fun:
                xx, yy = i, j
                min_fun = board[i][j]
    # 피할칸 윗칸과 피할칸에서는 특별하게 움직여야함
    flag = False
    i, j = 0, 0
    while True:
        if xx % 2 == 0:
            if i == xx:
                while True:
                    answer += "DR"
                    i += 1
                    j += 1
                    if i-1 == xx and j == yy:
                        if xx != R-1 and yy != C-1:
                            answer += "RUR"
                            i -= 1
                            j += 2
                        else:
                            break
                    else:
                        answer += "UR"
                        i -= 1
                        j += 1
                    if j >= C-1:
                        answer += "D"
                        i += 1
                        break
                if i < R-1:
                    answer += "D"
                    i += 1
                    flag = True
                else:
                    if not flag:
                        break
        else:
            if i == xx-1:
                while True:
                    if i+1 == xx and j == yy:
                        answer += "R"
                        j += 1
                        if j < C-1:
                            answer += "DR"
                            i += 1
                            j += 1
                    else:
                        if j < C-1:
                            answer += "DR"
                            i += 1
                            j += 1
                    if j < C-1:
                        answer += "UR"
                        i -= 1
                        j += 1
                    else:
                        answer += "D"
                        i += 1
                        break;
                if i < R-1:
                    answer += "D"
                    i += 1
                    flag = True
        if flag:
            answer += zigzag(1, 0)
            flag = False
        else:
            answer += zigzag(0, 0)
            flag = True
        if i < R-1:
            answer += "D"
            i += 1
        else:
            break
print(answer, end="")