import sys
input = sys.stdin.readline

INF = 2147000000
answer = INF

if __name__=="__main__":
    N = int(input())
    house = [list(map(int,input().split())) for _ in range(N)]
    for i in range(3):
        dt = [[INF] * 3 for _ in range(N)]
        dt[0][i] = house[0][i]
        for j in range(1, N):
            dt[j][0] = min(dt[j-1][1], dt[j-1][2]) + house[j][0]
            dt[j][1] = min(dt[j-1][0], dt[j-1][2]) + house[j][1]
            dt[j][2] = min(dt[j-1][0], dt[j-1][1]) + house[j][2]
        for k in range(3):
            if i == k:
                continue
            else:
                answer = min(answer, dt[-1][k])
    print(answer)
    
        