import math

N, M, K = map(int, input().split())

if K != 1:
    answer = list(range(N-M+1, N+1))
    remain_list = list(range(1, N-M+1))
    length = len(remain_list)
    lis_count = math.ceil(length/(K-1))
    if length == 0 or lis_count > M or length < (K-1):
        print(-1)
    else:
        count = 2
        while length > 0:
            answer.extend(remain_list[max(0, length-lis_count):length])
            length -= lis_count
            lis_count = math.ceil(length/max(K-count, 1))
            count += 1
        print(*answer)
else:
    if N == M:
        print(*list(range(1, N+1)))
    else:
        print(-1)