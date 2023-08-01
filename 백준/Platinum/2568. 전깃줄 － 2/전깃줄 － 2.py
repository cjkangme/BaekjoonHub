import sys

input = sys.stdin.readline

def binary_search(num, right):
    lo, hi = 0, right
    
    while lo < hi:
        mid = (lo + hi) // 2
        
        if sorted_arr[mid][1] < num:
            lo = mid + 1
        else:
            hi = mid

    return hi

if __name__=="__main__":
    N = int(input())
    arr = [tuple(map(int, input().split())) for _ in range(N)]
    arr.sort(key = lambda x : x[0])
    
    sorted_arr = [] # 교차하지 않는 전기줄
    index_list = [] # 로깅
    sorted_arr.append(arr[0])
    index_list.append(0)
    count = 1
    
    for i in range(1, N):
        if sorted_arr[-1][1] < arr[i][1]:
            sorted_arr.append(arr[i])
            index_list.append(count)
            count += 1
        else:
            idx = binary_search(arr[i][1], count)
            sorted_arr[idx] = arr[i]
            index_list.append(idx)
    # 최장 증가 수열 길이 출력
    print(N-count)
    
    # 저장한 로깅 리스트를 거꾸로 탐색하며 꼬이지 않은 전깃줄 구하기
    link_set = set() # 꼬이지 않은 전깃줄 번호 저장
    find_idx = count - 1
    for idx, inserted_idx in enumerate(index_list[::-1]):
        if inserted_idx == find_idx:
            link_set.add(N-idx-1)
            find_idx -= 1
        if find_idx < 0:
            break
    
    for i in range(N):
        if i not in link_set:
            print(arr[i][0])