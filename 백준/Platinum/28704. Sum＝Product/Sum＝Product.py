import sys

input = sys.stdin.readline

def solution(i, j, product, sum_num):
    lo, hi = over_ones[i], over_ones[j]
    left, right = over_ones[i-1]+1, over_ones[j+1]-1

    max_left, max_right = lo - left, right - hi
    
    need = product - sum_num
    
    if 0 <= need <= max_left + max_right:
        return min(max_left, max_right, max_left + max_right - need, need) + 1
    else:
        return 0

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    total = 0
    answer = N
    # 1보다 큰 값들의 index 저장 (첫 인덱스, 마지막 인덱스는 0, -1을 의미함)
    over_ones = [-1]
    for idx, val in enumerate(arr):
        total += val
        if val != 1:
            over_ones.append(idx)
    over_ones.append(N)
            
    length = len(over_ones)
    for i in range(1, length-1):
        sum_num = arr[over_ones[i]]
        product = arr[over_ones[i]]
        for j in range(i+1, length-1):
            sum_num += arr[over_ones[j]] + (over_ones[j]-over_ones[j-1]-1)
            product *= arr[over_ones[j]]
            if product > total:
                break
            answer += solution(i, j, product, sum_num)
        
    print(answer)