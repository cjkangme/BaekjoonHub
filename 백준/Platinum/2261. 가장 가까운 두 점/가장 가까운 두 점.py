import sys

input = sys.stdin.readline

# 두 점 사이의 거리를 구하는 함수
def get_distance(x, y, nx, ny):
    return (x-nx)**2 + (y-ny)**2

# mid를 가로지르는 선을 스캔하면서 최소거리를 구하는 함수
def line_scan(sub_list, height):
    # 서브리스트의 y가 작은순으로 정렬
    sub_list.sort(key = lambda x: x[1])
    
    for i in range(len(sub_list)-1):
        x, y = sub_list[i][0], sub_list[i][1]
        ni = i + 1
        while ni < len(sub_list):
            nx, ny = sub_list[ni][0], sub_list[ni][1]
            if (ny - y) ** 2 < height:
                height = min(height, get_distance(x, y, nx, ny))
                ni += 1
            else:
                break

    return height
        
    
# 분할 결과 남은 점이 3개 이하일 경우 브루트포스로 최소거리 구함
def brute_force(left, right):
    global answer
    for i in range(left, right+1):
        ix, iy = dot_list[i][0], dot_list[i][1]
        for j in range(i+1, right+1):
            jx, jy = dot_list[j][0], dot_list[j][1]
            length = get_distance(ix, iy, jx, jy)
            answer = min(answer, length)

# 분할 정복 : x축에서 left, right에 있는 선분의 거리 탐색
def devide(left, right):
    global answer
    if right - left <= 2:
        brute_force(left, right)
        return
    
    mid = (left + right) // 2
    devide(left, mid)
    devide(mid+1, right)
    
    # 현재 최소거리보다 짧거나 같은 거리에 있는 x값들을 서브리스트에 담음
    sub_list = [dot_list[mid]]
    point = dot_list[mid][0] # 기준
    lmid, rmid = mid-1, mid+1
    while left <= lmid:
        if (dot_list[lmid][0] - point) ** 2 <= answer:
            sub_list.append(dot_list[lmid])
            lmid -= 1
        else:
            break
    while rmid <= right:
        if (dot_list[rmid][0] - point) ** 2 <= answer:
            sub_list.append(dot_list[rmid])
            rmid += 1
        else:
            break
    
    answer = line_scan(sub_list, answer)
    
if __name__=="__main__":
    N = int(input())
    answer = 2147000000
    dot_list = [tuple(map(int, input().split())) for _ in range(N)]
    # x 좌표 기준 오름차순 정렬
    dot_list.sort(key = lambda x: x[0])
    
    devide(0, N-1)
    print(answer)