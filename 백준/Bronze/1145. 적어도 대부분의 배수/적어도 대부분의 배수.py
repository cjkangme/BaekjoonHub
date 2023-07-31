if __name__=="__main__":
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    answer = arr[-1] * arr[-2] * arr[-3] # 답이 될 수 있는 가장 큰 수
    
    for arr_num in arr:
        num = arr_num
        while num <= answer:
            count = 0
            for i in range(5):
                if num % arr[i] == 0:
                    count += 1
            if count >= 3:
                answer = num
            num += arr_num
    print(answer)