def solution(nums):
    unique = set(nums)
    return min(len(unique), len(nums) // 2)