import sys

input = sys.stdin.readline


def binary_search(money):
    left = 0
    right = N-1
    while left <= right:
        mid = (left+right)//2
        if coins[mid] > money:
            right = mid - 1
        elif coins[mid] < money:
            left = mid + 1
        else:
            return mid
    return right


N, money = map(int, input().split())
coins = [int(input()) for _ in range(N)]
answer = 0
while money:
    coin = coins[binary_search(money)]
    quotient = money // coin
    money -= coin * quotient
    answer += quotient
    
print(answer)