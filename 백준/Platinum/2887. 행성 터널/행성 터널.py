import sys
import heapq


def get_distance(arr, hq):
    """
    각 차원별로 터널 연결에 필요한 최소 비용 힙큐를 만들어 반납
    """
    corr_s, node_s = arr[0]
    for i in range(1, N):
        corr_l, node_l = arr[i]
        heapq.heappush(hq, (corr_l-corr_s, node_s, node_l))
        corr_s, node_s = corr_l, node_l
    return hq


def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)

    return parents[x]


def union(a, b, parents):
    # 연결할 두 노드의 부모 찾기
    a = find(a, parents)
    b = find(b, parents)
    # 낮은쪽의 인덱스가 부모가 되게끔 함
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


input = sys.stdin.readline

N = int(input())
x_list, y_list, z_list = [], [], []
for i in range(N):
    x, y, z = map(int, input().split())
    x_list.append((x, i))
    y_list.append((y, i))
    z_list.append((z, i))
# 좌표기준 리스트 오름차순 정렬
x_list.sort(key=lambda x: x[0])
y_list.sort(key=lambda x: x[0])
z_list.sort(key=lambda x: x[0])
# 가장 연결비용이 적은 노선순으로 정렬된 힙큐 구하기
hq = []
hq = get_distance(x_list, hq)
hq = get_distance(y_list, hq)
hq = get_distance(z_list, hq)
# 크루스칼 알고리즘
parents = list(range(N))
count = 1  # N-1개가 되어야 하므로
answer = 0
while count < N:
    cost, a, b = heapq.heappop(hq)
    # 부모가 다를 경우 (서로 연결이 안됐을 경우) 연결
    if find(a, parents) != find(b, parents):
        union(a, b, parents)
        count += 1
        answer += cost
print(answer)