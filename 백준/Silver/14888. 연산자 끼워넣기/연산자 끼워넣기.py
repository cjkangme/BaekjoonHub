import sys

input = sys.stdin.readline
INF = 2147000000

def calculator(left, right, operator):
    if operator == 0:
        return left + right
    elif operator == 1:
        return left - right
    elif operator == 2:
        return left * right
    else:
        if left < 0:
            return -(abs(left) // right)
        else:
            return left // right

def DFS(L, total):
    global min_total, max_total
    if L == N:
        min_total = min(min_total, total)
        max_total = max(max_total, total)
    else:
        for i in range(4):
            if operators[i]:
                operators[i] -= 1
                DFS(L+1, calculator(total, numbers[L], i))
                operators[i] += 1
        

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

min_total, max_total = INF, -INF

DFS(1, numbers[0])

print(max_total)
print(min_total)