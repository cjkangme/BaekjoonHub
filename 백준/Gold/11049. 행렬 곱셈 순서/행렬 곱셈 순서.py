import sys, heapq

input = sys.stdin.readline
INF = 2 ** 31

if __name__=="__main__":
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    dt = [[INF] * N for _ in range(N)]
    
    # 점화식을 위한 초기값 세팅
    for i in range(N):
        dt[i][i] = 0
    
    # 다이나믹 프로그래밍 탐색
    for i in range(1, N):
        for j in range(N-i):
            for k in range(j, j+i):
                temp = dt[j][k] + dt[k+1][j+i] + (arr[j][0] * arr[k][1] * arr[j+i][1])
                dt[j][j+i] = min(dt[j][j+i], temp)

    print(dt[0][N-1])