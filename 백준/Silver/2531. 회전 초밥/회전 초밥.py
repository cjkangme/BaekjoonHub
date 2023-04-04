import sys
from collections import deque

input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = deque([int(input()) for _ in range(N)])

# 초기 설정
count = 0
eat = [0] * (d+1)
# 쿠폰
eat[c] += 1
count += 1

# 0번 인덱스부터 k-1번까지 먹는 초밥 가짓수 구하기
for i in range(k):
    if not eat[sushi[i]]:
        count += 1
    eat[sushi[i]] += 1
# 출력할 답의 초기값 설정 (0~k-1개 먹었을 때 가짓수)
answer = count

# 모든 경우의 수를 돌기 위해 N-1번 반복
for _ in range(N-1):
    # 0번째에 있는 초밥을 eat에서 제거
    eat[sushi[0]] -= 1
    if not eat[sushi[0]]:
        count -= 1
    # k번째에 있는 초밥을 eat에 추가
    if not eat[sushi[k]]:
        count += 1
    eat[sushi[k]] += 1
    # 초밥 큐 회전 - 0번째 인덱스를 배열에서 빼고 제일 끝에 추가
    sushi.append(sushi.popleft())
    # 매 반복마다 출력할 답 갱신
    answer = max(answer, count)

print(answer)