import sys

input = sys.stdin.readline
INF = 3000000001

# 이분탐색으로 일치하는 수 반환, 없다면 더 큰 쪽 반환
def binary_search(num):
    lo, hi = 0, N-1
    
    while lo < hi:
        mid = (lo + hi) // 2
        
        if num > solutions[mid]:
            lo = mid + 1
        else:
            hi = mid
     
    return hi

if __name__=="__main__":
    N = int(input()) # 용액의 개수
    solutions = list(map(int, input().split())) # 용액 리스트
    solutions.sort()
    min_score = INF # 세 용액 특성값의 최솟값
    answer = [0, 0, 0] # 출력할 세 용액의 특성값
    
    # 브루트포스 탐색
    for left in range(0, N):
        for right in range(left+1, N):
            temp_binary = solutions[left] + solutions[right]
            # 0에 가까워야 하므로 부호 반전한 값을 탐색
            idx = binary_search(-temp_binary)
            # 높은쪽인지 낮은쪽인지 모르니까 각각 탐색
            for i in range(idx-1, idx+1):
                # 같은 용액 두 번은 안됨
                if i != left and i != right:
                    temp = abs(temp_binary + solutions[i])
                    if temp < min_score:
                        min_score = temp
                        answer = [solutions[left], solutions[i], solutions[right]]
    answer.sort()
    print(*answer)