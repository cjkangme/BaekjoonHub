"""
1. 각 알파벳 별로 일종의 점수를 계산 (ex. score = 10**(자릿수))
2. score 순으로 내림차순 정렬하여 정렬 순서에 따라 9 부터 1씩 낮은 숫자 부여
"""
import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
strings = []
score_dict = defaultdict(int)
for _ in range(N):
    string = input().rstrip()
    strings.append(string)
    for idx, char in enumerate(string[::-1]):
        score_dict[char] += 10 ** idx

scores = []
word2idx = dict()
for key, val in score_dict.items():
    # 내림차순이 되도록
    heapq.heappush(scores, (-val, key))
num = 9
while scores:
    _, key = heapq.heappop(scores)
    word2idx[key] = num
    num -= 1

# 출력
answer = 0
for string in strings:
    temp = ""
    for char in string:
        temp += str(word2idx[char])
    answer += int(temp)
    
print(answer)