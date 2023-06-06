import sys

input = sys.stdin.readline

def binary_search(LIS, num):
    left = 0
    right = len(LIS)
    while left <= right:
        mid = (left+right) // 2
        if num <= LIS[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return left

N = int(input())
A = list(map(int, input().split()))
# 최대 증가수열이 담길 리스트
LIS = []
LIS.append(A[0])

for i in range(1, N):
    if A[i] > LIS[-1]:
        LIS.append(A[i])
    else:
        idx = binary_search(LIS, A[i])
        LIS[idx] = A[i]
print(len(LIS))