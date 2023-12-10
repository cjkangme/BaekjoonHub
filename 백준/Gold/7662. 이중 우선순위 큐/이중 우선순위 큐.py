import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

def delete(hq, count_dict, is_max):
    while hq:
        number = heapq.heappop(hq)
        if is_max:
            number *= -1
        if count_dict[number] > 0:
            count_dict[number] -= 1
            return number
    return None

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        min_hq = []
        max_hq = []
        count_dict = defaultdict(int)
        
        for _ in range(N):
            command, number = map(str, input().rstrip().split())
            number = int(number)
            
            if command == "I":
                heapq.heappush(min_hq, number)
                heapq.heappush(max_hq, -number)
                count_dict[number] += 1
            else:
                if number == 1:
                    delete(max_hq, count_dict, True)
                else:
                    delete(min_hq, count_dict, False)
                    
        min_num = delete(min_hq, count_dict, False)
        max_num = delete(max_hq, count_dict, True)
        
        if min_num is not None and max_num is not None:
            print(max_num, min_num)
        elif min_num is not None:
            print(min_num, min_num)
        else:
            print("EMPTY")
    