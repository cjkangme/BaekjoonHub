import sys

input = sys.stdin.readline
MAX_NUM = 1000

def matrix_multi(arr1, arr2):
    temp = [[0] * A for _ in range(A)]
    for i in range(A):
        for j in range(A):
            for n in range(A):
                temp[i][j] += arr1[i][n] * arr2[n][j]
            temp[i][j] %= MAX_NUM
    return temp

def solution(power, arr):
    if power == 1:
        return arr
    
    mid = power // 2
    temp = solution(mid, arr)
    
    if power % 2 == 1:
        return matrix_multi(matrix_multi(temp, temp), arr)
    else:
        return matrix_multi(temp, temp)
            

if __name__=="__main__":
    A, B = map(int, input().split())
    array = [tuple(map(int, input().split())) for _ in range(A)]

    # A == 1000, B == 1일 때 0출력해야함
    if B == 1:
        for arr in array:
            for cell in arr:
                print(cell % 1000, end = " ")
            print()
    else:
        for arr in solution(B, array):
            print(*arr)