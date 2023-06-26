import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    important_list = list(map(int, input().split()))
    # 문서의 인덱스를 저장하는 que
    docs = deque(range(N))
    # 중요도를 오름차순으로 저장하는 stack
    important_rank = list(sorted(important_list))
    # M번째 인덱스가 목표
    target = M
    count = 1
    # M번째 인덱스의 수를 인쇄할 때 까지 반복
    while True:
        curr = docs.popleft()
        # 꺼낸 문서 중요도가 가장 높은 중요도와 일치한다면 인쇄, 아니면 맨 뒤로
        if important_list[curr] == important_rank[-1]:
            # 인쇄할 문서가 목표한 문서라면 순서 출력
            if curr == target:
                print(count)
                break
            count += 1
            important_rank.pop()
        else:
            docs.append(curr)