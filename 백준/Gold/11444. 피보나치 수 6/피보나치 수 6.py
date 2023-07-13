MAX_NUM = 1000000007

def matrix_multi(arr1, arr2):
    temp = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for n in range(2):
                temp[i][j] += arr1[i][n] * arr2[n][j]
            temp[i][j] %= MAX_NUM
    return temp

def solution(power):
    if power == 1:
        return array
    
    temp = solution(power // 2)
    if power % 2 == 0:
        return matrix_multi(temp, temp)
    else:
        return matrix_multi(matrix_multi(temp, temp), array)

if __name__=="__main__":
    n = int(input())
    # 피보나치 수를 구하기 위한 기본 행렬
    array = [[1, 1], [1, 0]]
    
    print(solution(n)[1][0])