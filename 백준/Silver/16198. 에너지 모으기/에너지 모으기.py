import sys

def get_energy(start):
    left, right = start-1, start+1
    while True:
        if weights[left]:
            break
        left -= 1
    
    while True:
        if weights[right]:
            break
        right += 1
   
    return weights[left] * weights[right]

def DFS(remain, total):
    global answer
    if remain == 2:
        answer = max(answer, total)
        return
    for i in range(1, N-1):
        if not visited[i]:
            temp = weights[i]
            visited[i] = True
            weights[i] = 0
            DFS(remain-1, total + get_energy(i))
            visited[i] = False
            weights[i] = temp
    
N = int(input())
weights = list(map(int, input().split()))
visited = [False] * N
answer = 0
DFS(N, 0)

print(answer)