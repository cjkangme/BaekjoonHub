import sys

input = sys.stdin.readline

def quick_sort(L, R):
    pivot = antennas[(L + R) // 2]
    left, right = L, R
    
    while left <= right:
        # L의 값이 pivot의 값보다 클 경우 중단
        while antennas[left] < pivot:
            left += 1
        # R의 값이 pivot의 값보다 작을 경우 중단
        while pivot < antennas[right]:
            right -= 1
        # 아직 포인터가 역전되지 않았다면 교환
        if left <= right:
            antennas[left], antennas[right] = antennas[right], antennas[left]
            left += 1
            right -= 1
    
    if L < right:
        quick_sort(L, right)
    if left < R:
        quick_sort(left, R)
    

if __name__ == "__main__":
    N = int(input())
    antennas = list(map(int, input().split()))
    
    # 정렬 수행
    quick_sort(0, N-1)
    
    # 정답출력
    print(antennas[(N-1) // 2])