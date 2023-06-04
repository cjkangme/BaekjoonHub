import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())
jewels = []
bags = []
length = N
answer = 0

# 무게가 무거운 순으로 정렬
jewels = [tuple(map(int, input().split())) for _ in range(N)]
jewels.sort(key = lambda x : x[0], reverse = True)
# 무거운 가방 순으로 정렬
bags = [int(input()) for _ in range(K)]
bags.sort(reverse = True)
# 우선순위 큐 (max heapque)
hq = []

while bags:
    # 가장 가벼운 가방을 꺼냄
    bag = bags.pop()
    while jewels:
        # 현재 가장 가벼운 보석을 꺼냄
        weight, value = jewels.pop()
        if bag >= weight:
            # 가방에 넣을 수 있다면 최대힙에 추가
            heapq.heappush(hq, -value)
        else:
            # 넣을 수 없다면 다시 보석 리스트에 추가하고 탐색 종료
            jewels.append((weight, value))
            break
    # 최대힙에서 heappop 한 값을 답변에 더함
    if hq:
        answer -= heapq.heappop(hq)
print(answer)