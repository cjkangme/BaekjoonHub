# 버블 정렬의 swap 횟수는 병합 정렬의 swap 횟수와 같다.
# 병합 정렬의 시간복잡도가 빠르므로, 병합정렬을 수행하면서 swap 횟수를 구하면 된다.

import sys

input = sys.stdin.readline

def devide(left, right):
    if right - left < 2:
        return
    
    mid = (left + right) // 2
    
    devide(left, mid)
    devide(mid, right)
    merge(left, mid, right)

def merge(left, mid, right):
    global swap
    temp = []
    l, r = left, mid
    
    while l < mid and r < right:
        if A[l] <= A[r]:
            temp.append(A[l])
            l += 1
        else:
            swap += (r - left -len(temp))
            temp.append(A[r])
            r += 1
    while l < mid:
        temp.append(A[l])
        l += 1
    while r < right:
        temp.append(A[r])
        r += 1
        
    # 병합된 부분 반영
    for i in range(left, right):
        A[i] = temp[i-left]
    

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    
    swap = 0
    devide(0, N)
    print(swap)