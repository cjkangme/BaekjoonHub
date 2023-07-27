import sys

input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    answer = 0
    
    # x좌표와 y좌표를 분리해서 저장
    x_list, y_list = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        x_list.append(x)
        y_list.append(y)
    
    # 정렬
    x_list.sort()
    y_list.sort()
    
    # 최소거리 위치 찾기
    x_point, y_point = x_list[n//2], y_list[n//2]
    
    # 위치 구하기
    for x, y in zip(x_list, y_list):
        answer += abs(x_point - x) + abs(y_point - y)
    print(answer)