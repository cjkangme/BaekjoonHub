import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    
    # pre : 먼저 지어져야하는 건물 수, build : 현재 건물이 지어져야 지을 수 있는 건물들
    pre = [0] * N
    build = [[] for _ in range(N)]
    for _ in range(K):
        parent, child = map(int, input().split())
        pre[child-1] += 1
        build[parent-1].append(child-1)
    # 마지막 건설 건물
    last = int(input()) - 1
    
    # 위상정렬 알고리즘
    cost_list = D.copy()
    # 큐 초기화
    que = deque()
    for idx, num in enumerate(pre):
        if not num:
            que.append(idx)
    while que:
        node = que.popleft()
        for next_node in build[node]:
            pre[next_node] -= 1
            cost_list[next_node] = max(cost_list[next_node], 
                                       cost_list[node]+D[next_node])
            if not pre[next_node]:
                que.append(next_node)
        if not pre[last]:
            break
    print(cost_list[last])