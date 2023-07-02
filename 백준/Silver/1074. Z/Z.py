if __name__=="__main__":
    N, r, c = map(int, input().split())
    
    power = N-1
    answer = 0
    # 1 * 1의 배열이 될 때까지 반복
    while power >= 0:
        quartile = 0 # 1사분면 0 ~ 4사분면 3
        compare_value = 2 ** power
        
        # r, c가 사등분한 배열에서 몇 사분면인지 계산
        if r >= compare_value:
            quartile += 2
            r -= compare_value
        if c >= compare_value:
            quartile += 1
            c -= compare_value
        
        # 해당 사분면의 (0, 0)까지 이동하는데 걸리는 거리를 출력변수에 더함
        answer += 2 ** (power*2) * quartile
        # 사등분을 쪼갬
        power -= 1
    print(answer)