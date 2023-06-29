from collections import deque

INF = 2147000000
MAX_NUM = 100000

N, K = map(int, input().split())

def BFS(N, K):
    visited = [INF] * (MAX_NUM * 2 + 1)
    que = deque()
    que.append((N, 0))
    visited[N] = 0
    
    while que:
        curr, count = que.popleft()
        
        temp = curr * 2
        while temp <= MAX_NUM * 2:
            if count < visited[temp]:
                visited[temp] = count
                que.append((temp, count))
            else:
                break
            temp *= 2
        if curr < MAX_NUM and count < visited[curr+1]:
            visited[curr+1] = count + 1
            que.append((curr+1, count+1))
        if curr > 0 and count < visited[curr-1]:
            visited[curr-1] = count + 1
            que.append((curr-1, count+1))
    return visited[K]
            
print(BFS(N, K))