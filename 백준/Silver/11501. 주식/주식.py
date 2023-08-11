import sys

input = sys.stdin.readline

def solution(n, stocks):
    answer = 0
    max_stock = 0
    # 거꾸로 탐색해서 최대값보다 싼 주식은 풀매수
    for stock in stocks[::-1]:
        if max_stock < stock:
            max_stock = stock
            continue
        answer += max_stock - stock
    return answer

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        stocks = list(map(int, input().split()))
        print(solution(N, stocks))