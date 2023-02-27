import sys
input = sys.stdin.readline

def DFS(shark):
    if visited[shark]:
        return False
    visited[shark] = True
    
    for food in eat[shark]:
        if match[food] == -1 or DFS(match[food]):
            match[food] = shark
            return True
    return False

N = int(input())
sharks = []
for _ in range(N):
    sharks.append(list(map(int, input().split())))
# 잡아먹을 수 있는 상어를 eat에 넣어줌
eat = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        if (sharks[i][0] == sharks[j][0] 
            and sharks[i][1] == sharks[j][1] 
            and sharks[i][2] == sharks[j][2]):
            
            if i < j:
                continue
        if (sharks[i][0] >= sharks[j][0] 
            and sharks[i][1] >= sharks[j][1] 
            and sharks[i][2] >= sharks[j][2]):
            
            eat[i].append(j)
            
match = [-1 for _ in range(N)]
answer = N
for i in range(N):
    for _ in range(2):
        visited = [False for _ in range(N)]
        if DFS(i):
            answer -= 1

print(answer)