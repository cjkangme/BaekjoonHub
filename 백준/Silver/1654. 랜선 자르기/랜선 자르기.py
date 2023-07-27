import sys

input = sys.stdin.readline

def binary_search(min_length, max_length):
    left, right = min_length, max_length
    answer = min_length
    while left <= right:
        count = 0
        mid = (left + right) // 2
    
        for cable in cables:
            count += cable // mid
        
        if count < N:
            right = mid-1
        else:
            left = mid+1
            answer = mid
    return answer

if __name__ == "__main__":
    K, N = map(int, input().split())
    
    cables = [int(input()) for _ in range(K)]
    
    max_length = sum(cables) // N
    
    print(binary_search(1, max_length))