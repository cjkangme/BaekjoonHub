import sys

input = sys.stdin.readline


def solution(bulbs, count):
    for i in range(1, N-1):
        if bulbs[i-1] != target[i-1]:
            count += 1
            for j in range(i-1, i+2):
                bulbs[j] = not bulbs[j]
    # 마지막 전구만 따로 처리
    if bulbs[N-1] != target[N-1]:
        count += 1
        bulbs[N-2] = not bulbs[N-2]
        bulbs[N-1] = not bulbs[N-1]
    if bulbs == target:
        return count
    else:
        return -1


N = int(input())
off = list(map(bool, map(int, input().rstrip())))
on = off.copy()
target = list(map(bool, map(int, input().rstrip())))

on[0] = not on[0]
on[1] = not on[1]
if off == target:
    print(0)
else:
    # 0번째 전구를 안눌렀을 때
    count = solution(off, 0)
    if count != -1:
        print(count)
    else:
        # 0번째 전구를 눌렀을 때
        count = solution(on, 1)
        print(count if count else -1)