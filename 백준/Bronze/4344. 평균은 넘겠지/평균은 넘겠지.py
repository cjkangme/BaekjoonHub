import sys

input = sys.stdin.readline

C = int(input())
for _ in range(C):
    test_case = list(map(int, input().split()))
    N, scores = test_case[0], test_case[1:]
    
    avg = sum(scores) / N
    
    count = 0
    for score in scores:
        if score > avg:
            count += 1
    
    print(f'{round(count / N, 5) * 100:.3f}%')