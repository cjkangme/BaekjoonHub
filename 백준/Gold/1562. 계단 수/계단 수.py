DEVIDE = 1000000000

if __name__=="__main__":
    N = int(input())
    answer = 0
    
    # dp[i][j][k][l] : i: i번째 길이일때, j가 최소수, k가 최대수, l이 마지막 수인 계단수 숫자
    dp = [[[[0] * 10 for _ in range(10)] for _ in range(10)] for _ in range(N)]
    # 초기 설정
    for i in range(1, 10):
        dp[0][i][i][i] = 1
    
    for l in range(1, N):
        for min_num in range(10):
            for max_num in range(min_num, 10):
                for last_num in range(10):
                    # 1 감소
                    if last_num != 0:
                        nmin_num = min(min_num, last_num-1)
                        dp[l][nmin_num][max_num][last_num-1] = \
                            (dp[l][nmin_num][max_num][last_num-1] + dp[l-1][min_num][max_num][last_num])
                    # 1 증가
                    if last_num != 9:
                        nmax_num = max(max_num, last_num+1)
                        dp[l][min_num][nmax_num][last_num+1] = \
                            (dp[l][min_num][nmax_num][last_num+1] + dp[l-1][min_num][max_num][last_num]) % DEVIDE
                    
    # 최소값 0, 최댓값 9인 수만 정답에 추가
    for i in range(10):
        answer = (answer + dp[-1][0][9][i]) % DEVIDE

    print(answer)