import sys, heapq

input = sys.stdin.readline
INF = 2147000000

class Node:
    def __init__(self, arr, cost):
        self.arr = arr
        self.visited = False
        self.cost = cost

# 배열로부터 딕셔너리 키로 사용될 정수 생성 (배열을 뒤집은 정수형태)
def arr2num(arr):
    digit = 1
    num = 0
    for a in arr:
        num += a * digit
        digit *= 10
    return num

def solution(arr, manipulates):
    graph = dict()
    num = arr2num(arr)
    graph[num] = Node(arr, 0)
    hq = [] # 다익스트라를 위한 우선순위 큐
    heapq.heappush(hq, (graph[num].cost, num))
    
    while hq:
        cost, num = heapq.heappop(hq)
        node = graph[num]
        
        if node.visited:
            continue
        
        for l, r, c in manipulates:
            temp = node.arr.copy()
            next_cost = cost + c
            temp[l], temp[r] = temp[r], temp[l]
            num = arr2num(temp)
            
            if graph.get(num) is None:
                graph[num] = Node(temp, next_cost)
                heapq.heappush(hq, (next_cost, num))
                continue
            if next_cost < graph[num].cost:
                graph[num].cost = next_cost
                heapq.heappush(hq, (next_cost, num))

        node.visited = True
        
    return graph

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0, 0) # 1부터 시작하므로 안쓰는 0번 인덱스에 최소값 0 삽입
    M = int(input())
    manipulates = [list(map(int, input().split())) for _ in range(M)]
    
    # 비내림차순 배열
    target = list(sorted(arr))
    target_num = arr2num(target)
    
    graph = solution(arr, manipulates)
    
    print(graph[target_num].cost if graph.get(target_num) else -1)