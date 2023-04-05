from math import isqrt


def get_prime(N):
    # N 이하의 소수를 구하는 함수
    is_prime = list(range(N+1))
    for i in range(2, isqrt(N)+1):
        # 1. i가 소수인 경우 i의 배수를 모두 소수가 아닌 것으로 처리
        # 2. 소수 배열에 i를 담는다.
        if is_prime[i]:
            for j in range(i+i, N+1, i):
                is_prime[j] = 0
    # 2부터 시작하여 is_prime에서 0, None, False 인 값을 모두 날리고 저장함
    primes = list(filter(None, is_prime[2:]))
    return primes


N = int(input())

# 소수 배열을 구하여 가져옴
primes = get_prime(N)
max_idx = len(primes)

# 투포인터를 이용하여 연속된 소수의 합 경우의 수 탐색
answer = 0
left, right, total = 0, 0, 0
# left 포인터의 순서가 역전되면 탈출, 인덱스 범위를 벗어나면 탈출
while left <= right and left < max_idx:
    # 현재 구한 합계가 주어진 수보다 크면 탈출, 인덱스 범위를 벗어나면 탈출
    while total < N and right < max_idx:
        total += primes[right]
        right += 1
    if total == N:
        answer += 1
    # left 포인터가 가리키는 값을 빼고, left 포인터 한 칸 전진
    total -= primes[left]
    left += 1

print(answer)