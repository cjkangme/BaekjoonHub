import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    columns = [tuple(map(int, input().split())) for _ in range(N)]
    columns.sort(key=lambda x : x[0]) # 위치순 오름차순 정렬
    
    area = 0 # 창고의 총 넓이
    max_height = max(map(lambda x : x[1], columns)) # 가장 높은 기둥의 높이
    pivot = -1
    # 가장 높은 기둥이 있는 인덱스 찾기
    for i in range(N-1, -1, -1):
        if columns[i][1] == max_height:
            pivot = i
            break
    
    # 왼쪽부터 가장 높은 기둥이 있는 곳 까지 정방향 탐색
    height = columns[0][1]
    for i in range(1, pivot+1):
        # 창고 넓이 계산
        area += height * (columns[i][0] - columns[i-1][0])
        # 창고 높이 갱신
        height = max(height, columns[i][1])
    # 오른쪽부터 가장 높은 기둥이 있는 곳 까지 역방향 탐색
    height = columns[-1][1]
    for i in range(N-2, pivot-1, -1):
        area += height * (columns[i+1][0] - columns[i][0])
        height = max(height, columns[i][1])
    # 가장 높은 기둥의 넓이 더하기
    area += columns[pivot][1]
    
    # 결과 출력
    print(area)