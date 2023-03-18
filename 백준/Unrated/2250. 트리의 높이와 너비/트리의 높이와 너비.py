import sys
from collections import defaultdict
input = sys.stdin.readline


def get_width(nodes, col_nums):
    min_width = N
    max_width = 0
    for node in nodes:
        idx = col_nums.index(node)
        min_width = min(min_width, idx)
        max_width = max(max_width, idx)
    return max_width - min_width + 1


def DFS(depth, node, tree):
    depth_dict[depth].append(node)
    left, right = tree[node]
    if left != -1:
        DFS(depth+1, left, tree)
    col_nums.append(node)
    if right != -1:
        DFS(depth+1, right, tree)


N = int(input())
tree = [() for _ in range(N+1)]
for _ in range(N):
    parent, left, right = map(int, input().split())
    tree[parent] = (left, right)

start = 1
while True:
    temp = start
    for i in range(N+1):
        if temp in tree[i]:
            start = i
            break
    if temp == start:
        break

col_nums = []
depth_dict = defaultdict(lambda: [])

DFS(1, start, tree)

i = 1
answer = [1, 1]
while True:
    if not depth_dict[i]:
        break
    temp = get_width(depth_dict[i], col_nums)
    if temp > answer[1]:
        answer = [i, temp]
    i += 1

print(*answer)