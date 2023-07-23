import sys

input = sys.stdin.readline

# 설치 간격이 distance일 때 설치할 수 있는 공유기의 수를 구하는 함수
def install(distance):
    count = 1 # 제일 왼쪽에 하나 설치되었다고 가정
    left, right = 0, 1
    while right < N:
        # 두 포인터가 가리키는 집 사이 거리가 distance보다 크거나 같으면 설치
        if distance <= hubs[right] - hubs[left]:
            count += 1
            left, right = right, right+1
        # 설치 거리가 안되면 right 포인터 전진
        else:
            right += 1

    return count


# 이분 탐색을 통해 C개 설치가 가능한 최대 거리 탐색
def binary_search(left, right):
    answer = 1
    while left <= right:
        mid = (left + right) // 2
        count = install(mid)
        
        # count가 C보다 작으면 왼쪽 탐색
        if count < C:
            right = mid - 1
        # count가 C보다 크거나 같으면 오른쪽 탐색하고 반환할 값 갱신
        else:
            left = mid + 1
            answer = mid

    # upper bound이므로 right값 반환
    return answer
    

if __name__ == "__main__":
    # 입력 받기
    N, C = map(int, input().split())
    hubs = [int(input()) for _ in range(N)]
    
    # 순차 탐색을 위해 배열 정렬
    hubs.sort()
    
    print(binary_search(1, hubs[-1] - hubs[0]))