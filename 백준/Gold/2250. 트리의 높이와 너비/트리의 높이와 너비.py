import sys
input = sys.stdin.readline


def DFS(depth, node):
    global col_num
    left, right = tree[node]

    if left != -1:
        DFS(depth+1, left)

    max_width[depth][0] = min(max_width[depth][0], col_num)
    max_width[depth][1] = max(max_width[depth][1], col_num)
    col_num += 1

    if right != -1:
        DFS(depth+1, right)


N = int(input())
tree = [() for _ in range(N+1)]
is_child = [0] * (N+1)

for _ in range(N):
    parent, left, right = map(int, input().split())
    tree[parent] = (left, right)
    if left != -1:
        is_child[left] += 1
    if right != -1:
        is_child[right] += 1

start = is_child[1:].index(0) + 1

max_width = [[2147000000, 0] for _ in range(N)]
col_num = 1

DFS(0, start)

answer_row = 0
answer_width = 0

for i in range(N):
    min_col, max_col = max_width[i]

    if max_col == 0:
        break

    temp = max_col - min_col + 1
    if temp > answer_width:
        answer_width = temp
        answer_row = i+1

print(answer_row, answer_width)