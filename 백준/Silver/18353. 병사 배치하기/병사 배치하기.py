import sys

input = sys.stdin.readline

def binary_search(num, count):
    left, right = 0, count-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if num < sorted_soldiers[mid]:
            left = mid+1
        else:
            right = mid-1

    return left

if __name__ == "__main__":
    N = int(input())
    soldiers = list(map(int, input().split()))
    sorted_soldiers = [soldiers[0]]
    count = 1
    
    for i in range(1, N):
        if soldiers[i] < sorted_soldiers[-1]:
            sorted_soldiers.append(soldiers[i])
            count += 1
        else:
            idx = binary_search(soldiers[i], count)
            sorted_soldiers[idx] = soldiers[i]

    print(N-count)