import sys

input = sys.stdin.readline

if __name__=="__main__":
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    max_temp = sum(arr[:K])
    temp = max_temp
    
    for i in range(K, N):
        temp -= arr[i-K]
        temp += arr[i]
        max_temp = max(max_temp, temp)
    
    print(max_temp)