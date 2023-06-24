import sys
from collections import defaultdict

def get_count(have_list):
    have_count_dict = defaultdict(int)
    for q in have_list:
        have_count_dict[q] += 1
    return have_count_dict
        
if __name__ == "__main__":
    N = int(input())
    have_list = list(map(int, input().split()))
    M = int(input())
    question_list = list(map(int, input().split()))
    
    have_count_dict = get_count(have_list)
    
    for q in question_list:
        print(have_count_dict[q], end = " ")