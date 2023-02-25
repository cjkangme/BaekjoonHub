import sys
from collections import deque
input = sys.stdin.readline

INF = 2147000000
MAX_N = 802


def BFS(source, sink, visited):
    que = deque()
    que.append(source)

    while que and visited[sink] == -1:
        sv = que.popleft()
        for dv in graph[sv]:
            if capacity[sv][dv] - flow[sv][dv] > 0 and visited[dv] == -1:
                visited[dv] = sv
                que.append(dv)

                if dv == sink:
                    break

    if visited[sink] == -1:
        return True
    else:
        return False


def edmonds_karp(source, sink):
    answer = 0
    while True:
        visited = [-1 for _ in range(MAX_N)]
        if BFS(source, sink, visited):
            break

        min_flow = INF

        # 해당 경로의 가장 적은 잔여용량(min_flow) 구하기
        dv = sink
        while dv != source+1:
            sv = visited[dv]
            min_flow = min(min_flow, capacity[sv][dv] - flow[sv][dv])
            dv = sv
        # min_flow 만큼 경로의 유량 증가, 유량 대칭 적용
        dv = sink
        while dv != source+1:
            sv = visited[dv]
            flow[sv][dv] += min_flow
            flow[dv][sv] -= min_flow
            dv = sv

        # source에서 sink로 흐르는 전체 유량 적용
        answer += min_flow
    return answer


N, P = map(int, input().split())
graph = [[] for _ in range(MAX_N)]
capacity = [[0] * MAX_N for _ in range(MAX_N)]
flow = [[0] * MAX_N for _ in range(MAX_N)]

for _ in range(P):
    sv, dv = map(int, input().split())
    # in, out 구분
    sv_in = sv * 2 - 1
    sv_out = sv_in + 1
    dv_in = dv * 2 - 1
    dv_out = dv_in + 1

    graph[sv_out].append(dv_in)
    graph[dv_in].append(sv_out)

    graph[dv_out].append(sv_in)
    graph[sv_in].append(dv_out)

    capacity[sv_out][dv_in] = 1
    capacity[dv_out][sv_in] = 1
for i in range(1, N+1):
    sv = i * 2 - 1
    dv = sv + 1
    graph[sv].append(dv)
    graph[dv].append(sv)
    capacity[sv][dv] = 1

print(edmonds_karp(1, 3))