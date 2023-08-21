import sys

input = sys.stdin.readline

def count_blueray(movies, limit):
    count, cur_time = 1, 0

    for time in movies:
        next_time = cur_time + time
        if next_time > limit:
            cur_time = time
            count += 1
        else:
            cur_time = next_time

    return count

def binary_search(movies, lo, hi):
    while lo <= hi:
        mid = (lo + hi) // 2
        if count_blueray(movies, mid) <= M:
            hi = mid - 1
        else:
            lo = mid + 1
    return lo
        
    
if __name__ == "__main__":
    N, M = map(int, input().split())
    movies = list(map(int, input().split()))
    
    print(binary_search(movies, max(movies), sum(movies)))