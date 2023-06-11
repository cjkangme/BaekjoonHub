arr = list(map(int, input()))
arr.sort(reverse=True)

# 3의 배수가 아니거나 10의 배수가 아닌 경우 -1 출력
if sum(arr) % 3 or arr[-1] != 0:
    print(-1)
else:
    [print(num, end="") for num in arr]