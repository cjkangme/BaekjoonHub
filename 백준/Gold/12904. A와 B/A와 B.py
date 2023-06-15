import sys

input = sys.stdin.readline

S = list(map(str, input().rstrip()))
T = list(map(str, input().rstrip()))

# T와 S의 차이만큼 반복
for _ in range(len(T)-len(S)):
    # T의 마지막 글자가 A면 A 추가연산을 했다는 것이므로 거꾸로 연산
    if T[-1] == "A":
        T.pop()
    # T의 마지막 글자가 B면 B 추가연산을 했다는 것이므로 거꾸로 연산
    else:
        T.pop()
        T = T[::-1]

print(1 if S == T else 0)