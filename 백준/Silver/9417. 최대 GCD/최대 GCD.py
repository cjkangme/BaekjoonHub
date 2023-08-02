import sys

input = sys.stdin.readline

# 유클리드 알고리즘으로 a, b의 최대공약수를 찾는 함수, a가 항상 큰 값이다.
def find_gcd(a, b):
    n = a % b
    if n == 0:
        return b
    else:
        return find_gcd(b, n)

def brute_force_search(arr):
    answer = 1
    length = len(arr)
    for i in range(length):
        for j in range(i+1, length):
            answer = max(answer, find_gcd(max(arr[i], arr[j]), min(arr[i], arr[j])))
    return answer

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        arr = list(map(int, input().split()))
        print(brute_force_search(arr))