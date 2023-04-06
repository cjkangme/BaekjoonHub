import sys
input = sys.stdin.readline

N, S = map(int, input().split())
arr = list(map(int, input().split()))

# 정답이 있는지 여부 체크
flag = False
# 최소값이므로 answer를 최대값으로 초기화
answer = 2147000000

total = 0
count = 0
right = 0
for left in range(N):
    
    # right가 더 전진하지 못하면 탐색 X
    while right < N:
        # S보다 크면 while문 탈출
        if total >= S:
            break
        # total 갱신
        total += arr[right]
        count += 1
        # right 전진 처리
        right += 1
        
    # answer 갱신 (right 전진 없이 left만 전진하는 경우 고려)
    if total >= S:
        flag = True
        answer = min(answer, count)
    # right를 빠져나와도 갱신 못하면 break
    else:
        break
    # left가 한 칸 전진하므로 관련 처리
    total -= arr[left]
    count -= 1

print(answer if flag else 0)