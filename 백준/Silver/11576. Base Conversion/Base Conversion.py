import sys
input = sys.stdin.readline

def a_to_ten(lst, b):
    res = 0
    for i, num in enumerate(lst):
        base = b ** (m - i - 1)
        res += num * base
    return res

def ten_to_b(num, b):
    tmp = num
    res = []
    while tmp:
        res.append(tmp % b)
        tmp = tmp // b
    return res

A, B = map(int, input().split())
m = int(input())
num_list = list(map(int, input().split()))
num_10 = a_to_ten(num_list, A)
num_b = ten_to_b(num_10, B)
print(*num_b[::-1])