import sys

input = sys.stdin.readline
INF = 2147000000

if __name__=="__main__":
    N = int(input())
    lifeguards = [tuple(map(int, input().split())) for _ in range(N)]
    
    shift = [0] * 1000
    min_term = INF
    
    # 근무표 채우기
    for start, end in lifeguards:
        for i in range(start, end):
            shift[i] += 1
    
    for start, end in lifeguards:
        count = 0
        for i in range(start, end):
            if shift[i] - 1 == 0:
                count += 1
        min_term = min(min_term, count)
 
    print(len(list(filter(None, shift))) - min_term)