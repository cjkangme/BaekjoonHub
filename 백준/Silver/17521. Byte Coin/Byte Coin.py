import sys

input = sys.stdin.readline
INF = 2147000000

if __name__ == "__main__":
    n, W = map(int, input().split())
    costs = [int(input()) for _ in range(n)]
    
    money, coin = W, 0
    turning_days = [] # 상승장, 하락장이 바뀌는 날
    flag = False # False : 하락장, True : 상승장
    
    # 터닝포인트 기록
    for i in range(n-1):
        if costs[i] < costs[i+1] and not flag:
            turning_days.append(i)
            flag = True
        elif costs[i+1] < costs[i] and flag:
            turning_days.append(i)
            flag = False
    turning_days.append(n-1) # IndexError 방지
    
    # 하락장 -> 상승장을 1세트로 반복
    min_cost, max_cost = INF, 0
    iter_num = (len(turning_days))//2
    point = 1
    left, right = 0, turning_days[0]
    for _ in range(iter_num):
        min_cost = min(costs[left:right+1])
        coin += money // min_cost
        money -= coin * min_cost
        
        left, right = right+1, turning_days[point]
        point += 1
        
        max_cost = max(costs[left:right+1])
        money += max_cost * coin
        coin = 0

        try:
            left, right = right+1, turning_days[point]
            point += 1
        except IndexError:
            pass
        
    print(money)
