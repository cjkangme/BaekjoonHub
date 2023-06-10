import sys

input = sys.stdin.readline


N = int(input())
numbers = [int(input()) for _ in range(N)]
arr = []
chk = [False] * N
# 두개의 수를 묶어야 하는 경우를 표시하기 위한 값
OFFSET = N
answer = 0

for i in range(N):
    arr.append((numbers[i], i, i))
    for j in range(i+1, N):
        if numbers[i] < 0 or numbers[j] < 0:
            arr.append((numbers[i]*numbers[j], i+OFFSET, j))
        else:
            arr.append((numbers[i]*numbers[j], i-OFFSET, j))
# pop 연산 수행시 가장 큰 수부터 빼도록 함
arr.sort()
while arr:
    num, left, right = arr.pop()
    # 정렬을 위해 더했던 OFFSET 값을 원상복구
    left %= OFFSET
    if not chk[left] and not chk[right]:
        answer += num
        chk[left] = True
        chk[right] = True
        
print(answer)