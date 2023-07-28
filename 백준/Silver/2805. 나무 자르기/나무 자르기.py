import sys

input = sys.stdin.readline

# 이분 탐색을 통해 height 높이로 나무를 잘랐을 때 잘리는 첫번째 나무 탐색
def binary_search(height):
    lo, hi = 0, N-1
    
    while lo < hi:
        mid = (lo + hi) // 2
        
        if trees[mid] < height:
            lo = mid + 1
        else:
            hi = mid
    
    return lo

if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    total_wood = sum(trees)
    
    # 이분 탐색 위해 오름차순 정렬
    trees.sort()
    
    # 누적합 구하기
    running_sum = [0] * N
    running_sum[0] = trees[0]
    for i in range(1, N):
        running_sum[i] = running_sum[i-1] + trees[i]
    
    # 탐색 범위 설정
    lo, hi = 0, trees[-1]
    # 적절한 높이를 찾을 때까지 이분 탐색
    while lo <= hi:
        mid = (lo + hi) // 2
        idx = binary_search(mid)

        # 산술 계산
        wood = total_wood - (N - idx) * mid

        if idx != 0:
            wood -= running_sum[idx-1]
        
        if wood < M:
            hi = mid-1
        else:
            lo = mid+1
    
    print(hi)
