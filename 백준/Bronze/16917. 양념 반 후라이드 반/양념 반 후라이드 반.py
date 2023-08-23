# 반반치킨을 살 수 있는 모든 경우의 수(최대 20만) 고려하여 브루트포스 탐색

INF = 5000 * 200000

if __name__ == "__main__":
    A, B, C, X, Y = map(int, input().split())
    max_half = max(X, Y)
    min_cost = INF
    for i in range(max_half+1):
        min_cost = min(min_cost, (C * 2 * i) + max(A * (X - i), 0) + max(B * (Y - i), 0))
    print(min_cost)
