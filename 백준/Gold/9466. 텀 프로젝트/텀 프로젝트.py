import sys
from collections import deque

input = sys.stdin.readline

# bfs를 통해 팀에 속하지 못한 학생 수를 찾아 반환
def bfs(graph):
    count = 0 # 팀에 속하지 못한 학생 수
    que = deque()
    for i in range(1, N+1):
        # 간선의 수가 1이라면 사이클을 이룰 수 없으므로 큐에 추가
        if graph[i][0] == 1:
            que.append(graph[i][1])
        
    while que:
        child = que.popleft()
        count += 1 # 큐에서 꺼냈다는 건 팀을 이루지 못했다는 뜻
        
        graph[child][0] -= 1
        # 부모 노드가 제거되면서 간선 수가 1이 되었다는 건 사이클을 이룰 수 없다는 것이므로 큐에 추가
        if graph[child][0] == 1:
            que.append(graph[child][1])

    return count

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = list(map(int, input().split()))
        
        # [0] : 간선의 수 (자신이 선택한 학생 + 자신을 선택한 학생 수), [1] : 자신이 선택한 학생
        graph = [[1, -1] for _ in range(N+1)]
        for idx, val in enumerate(arr):
            graph[idx+1][1] = val
            graph[val][0] += 1

        print(bfs(graph))