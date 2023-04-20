import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

# 자신보다 먼저 불러야하는 가수의 수 (위상정렬)
num_prev = [0] * (N+1)
num_prev[0] = -1
# 자신 뒤에 불러야하는 가수를 저장하는 배열
list_next = [[] for _ in range(N+1)]
for _ in range(M):
    temp = list(map(int, input().split()))
    length = temp[0]
    # 먼저 불러야하는 사람 수, 뒷 순서로 불러야할 사람 업데이트
    # 첫번째 부르는 사람은 앞사람이 없으므로 두번째부터 시작
    for i in range(2, length+1):
        prev_s = temp[i-1]
        s = temp[i]
        num_prev[s] += 1
        list_next[prev_s].append(s)
# 위상정렬 위해 큐 초기화
que = deque()
for idx, num in enumerate(num_prev):
    if not num:
        que.append(idx)
# 위상정렬
answer = []
while que:
    s = que.popleft()
    for s_next in list_next[s]:
        num_prev[s_next] -= 1
        # 자신 앞에 부를 사람이 없게되면 큐에 추가
        if not num_prev[s_next]:
            que.append(s_next)
    answer.append(s)

# 모든 가수가 노래를 부를 수 있다면 순서대로 출력, 아니면 0 출력
if len(answer) == N:
   [print(s) for s in answer]
else:
    print(0)