import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

# 트리
def find_child(in_left, in_right, post_left, post_right):
    if in_left > in_right:
        return
    
    # 프리오더 이므로 루트 바로 출력
    root = post_order[post_right]
    print(root, end=" ")
    
    # 인오더에서 루트의 인덱스 구하기
    root_index = in_order_index[root]
    offset = root_index - in_left
    
    # 왼쪽 자식 탐색
    find_child(in_left, root_index-1, post_left, post_left+offset-1)
    # 오른쪽 자식 탐색
    find_child(root_index+1, in_right, post_left+offset, post_right-1)

N = int(input()) #노드의 개수
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
# 향후 루트 인덱스를 찾게되므로 미리 맵핑해둠
in_order_index = {value: index for index, value in enumerate(in_order)}

find_child(0, N-1, 0, N-1)