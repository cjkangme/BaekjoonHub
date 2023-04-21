import sys
import math
import heapq

def get_minheap_of_distance(arr):
    hq = []
    for i in range(n):
        for j in range(i+1, n):
            x_left, y_left = arr[i]
            x_right, y_right = arr[j]
            dist = math.sqrt(((x_left-x_right)**2) + ((y_left-y_right)**2))
            heapq.heappush(hq, (dist, i, j))
    return hq

def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)
    return parents[x]

def union(a, b, parents):
    a = find(a, parents)
    b = find(b, parents)
    
    if a > b:
        parents[b] = a
    else:
        parents[a] = b
        
n = int(input())
corr_list = [list(map(float, input().split())) for _ in range(n)]

hq = get_minheap_of_distance(corr_list)

parents = list(range(n))
count = 1
answer = 0
while hq:
    dist, left, right = heapq.heappop(hq)
    if find(left, parents) != find(right, parents):
        union(left, right, parents)
        count += 1
        answer += dist
    if count == n:
        break
print(round(answer, 2))