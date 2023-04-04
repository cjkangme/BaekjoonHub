import sys
input = sys.stdin.readline

N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = []
i, j = 0, 0

while True:
    try:
        if A[i] > B[j]:
            answer.append(B[j])
            j += 1
        else:
            answer.append(A[i])
            i += 1
    except IndexError:
        break
if i == N:
    answer.extend(B[j:])
else:
    answer.extend(A[i:])
    
print(*answer)
