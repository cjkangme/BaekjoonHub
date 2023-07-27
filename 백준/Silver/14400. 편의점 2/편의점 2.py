import sys

# 병합 정렬
def merge_sort(arr, left, right):
    if left == right:
        return arr
    
    mid = (left + right) // 2
    lmid, rmid = mid, mid+1
    arr = merge_sort(arr, left, lmid)
    arr = merge_sort(arr, rmid, right)
    
    l, r = left, rmid
    temp = []
    while l <= lmid and r <= right:
        if arr[l] <= arr[r]:
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            r += 1

    for i in range(l, lmid+1):
        temp.append(arr[i])

    for i in range(r, right+1):
        temp.append(arr[i])
    
    arr[left:right+1] = temp
    
    return arr

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    answer = 0
    
    # x좌표와 y좌표를 분리해서 저장
    x_list, y_list = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    
    # 정렬
    x_sorted = merge_sort(x_list, 0, n-1)
    y_sorted = merge_sort(y_list, 0, n-1)
    
    # 최소거리 위치 찾기
    x_point, y_point = x_sorted[n//2], y_sorted[n//2]
    
    # 위치 구하기
    for x, y in zip(x_list, y_list):
        answer += abs(x_point - x) + abs(y_point - y)
    print(answer)