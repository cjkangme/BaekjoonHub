import sys
from collections import deque

def BFS(start, target):
    que = deque()
    que.append((start, ""))
    visited = [False] * 10000
    visited[start] = True
    
    while que:
        number, context = que.popleft()
        
        if number == target:
            return context
        
        temp = D(number)
        if not visited[temp]:
            que.append((temp, context+"D"))
            visited[temp] = True
            
        temp = S(number)
        if not visited[temp]:
            que.append((temp, context+"S"))
            visited[temp] = True
            
        temp = L(number)
        if not visited[temp]:
            que.append((temp, context+"L"))
            visited[temp] = True
            
        temp = R(number)
        if not visited[temp]:
            que.append((temp, context+"R"))
            visited[temp] = True

def D(number):
    return number * 2 % 10000

def S(number):
    number -= 1
    return number if number >= 0 else 9999
        
def L(number):
    number *= 10
    number += number // 10000
    return number % 10000

def R(number):
    temp = number % 10
    number //= 10
    number += temp * 1000
    return number

T = int(input())
for _ in range(T):
    start, target = map(int, input().split())
    print(BFS(start, target))