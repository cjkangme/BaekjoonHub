import sys

input = sys.stdin.readline
INF = 2147000000

def calculate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    else:
        if (a > 0 and b > 0) or (a < 0 and b < 0):
            return a // b
        else:
            return -(abs(a) // abs(b))

def DFS(result, count):
    global max_result, min_result
    if count == N:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    for i in range(4):
        if operators[i] > 0:
            operators[i] -= 1
            DFS(calculate(result, numbers[count], i), count+1)
            operators[i] += 1

if __name__=="__main__":
    N = int(input())
    numbers = list(map(int, input().split()))
    operators = list(map(int, input().split()))
    
    max_result = -INF
    min_result = INF
    DFS(numbers[0], 1)
    print(max_result)
    print(min_result)