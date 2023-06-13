N, K = map(int, input().split())

answer = ["B"] * N
flag = False

for num_a in range(N-1, 0, -1):
    num_b = N - num_a
    if num_a * num_b >= K:
        flag = True
        remain = K
        count_a = 0
        max_a = N - num_a
        while count_a < num_a:
            temp = min(remain, max_a)
            if temp == max_a:
                answer[count_a] = "A"
            elif temp == 0:
                answer[count_a-num_a] = "A"
            else:
                answer[count_a+num_b-temp] = "A"
            count_a += 1
            remain -= temp
        break
print("".join(answer) if flag else -1)
