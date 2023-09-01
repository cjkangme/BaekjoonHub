import sys
from collections import defaultdict

input = sys.stdin.readline

def solution(L, num, answer):
    if count_dict[num] > 0:
        count_dict[num] -= 1
        answer.append(num)
        DFS(L+1, num, answer)
        count_dict[num] += 1
        answer.pop()
    return

def DFS(L, curr, answer):
    if L == N:
        print(*answer)
        sys.exit(0)
    solution(L, curr * 2, answer)
    if curr % 3 == 0:
        solution(L, curr // 3, answer)
    

if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))
    count_dict = defaultdict(int)
    for num in B:
        count_dict[num] += 1
    for num in B:
        DFS(1, num, [num])