if __name__ == "__main__":
    N, K = map(int, input().split())
    
    k = K
    digit, member = 1, 9
    while True:
        temp = digit * member
        if k > temp:
            k -= temp
            digit += 1
            member *= 10
        else:
            break
    
    
    # K 번째 자리에 있는 수가 몇인지 확인
    num = (k-1) // digit
    num += 10 ** (digit-1)
    # K 번째 자리에 있는 수가 N보다 크다면 수의 길이가 작은 것
    if num > N:
        print(-1)
    else:
        idx = (k-1) % digit
        print(str(num)[idx])