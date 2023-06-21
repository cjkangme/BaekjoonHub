import sys
input = sys.stdin.readline

def binary_search(num, having_nums):
    left = 0
    right = N-1
    while left <= right:
        mid = (left + right) // 2
        if num > having_nums[mid]:
            left = mid + 1
        elif num < having_nums[mid]:
            right = mid - 1
        else:
            return mid
    return -1

N = int(input())
having_nums = list(map(int, input().split()))
M = int(input())
nums = list(map(int, input().split()))

having_nums.sort()

for num in nums:
    temp = binary_search(num, having_nums)
    print(1 if binary_search(num, having_nums) >= 0 else 0, end = " ")