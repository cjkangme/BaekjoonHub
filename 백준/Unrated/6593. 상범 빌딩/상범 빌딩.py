import sys
from collections import deque

input = sys.stdin.readline

def BFS(start):
    que = deque()
    que.append(start)
    while que:
        x, y, z, time = que.popleft()
        for n in range(6):
            xx = x + dx[n]
            yy = y + dy[n]
            zz = z + dz[n]
            if (0<=xx<L and 0<=yy<R and 0<=zz<C
                and building[xx][yy][zz] != '#'):
                if building[xx][yy][zz] == 'E':
                    return time + 1
                building[xx][yy][zz] = '#'
                que.append((xx, yy, zz, time+1))
    return 0

dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while True:
    building=[]
    start = tuple()
    L, R, C = map(int, input().split())
    if L == 0:
        break
    for i in range(L):
        floor = []
        for j in range(R):
            temp = list(map(str, input().rstrip()))
            if not start:
                for k in range(C):
                    if temp[k] == 'S':
                        start = (i, j, k, 0)
                        temp[k] = '#'
            floor.append(temp)
        building.append(floor)
        input()
    answer = BFS(start)
    if answer:
        print(f'Escaped in {answer} minute(s).')
    else:
        print('Trapped!')