if __name__ == "__main__":
    N = int(input())
    answer = 0
    
    # 남규가 사탕 i개를 가졌다고 가정
    for i in range(3, N-1):
        # 택희는 1개 이상, 짝수개의 사탕을 가져야 함
        for j in range(2, N-i, 2):
            candy = N - i - j
            # 영훈이는 1개 이상이면서 냠규보다 2개 적은 수의 사탕을 가져야 함, 
            if 1 <= candy <= i-2:
                answer += 1
    
    print(answer)