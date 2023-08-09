# set으로 해결하는게 더 쉽지만 그냥 딕셔너리 써보는 연습
from collections import defaultdict

def solution(participant, completion):
    participant_dict = defaultdict(int)
    for string in completion:
        participant_dict[string] += 1
    
    for string in participant:
        participant_dict[string] -= 1
        if participant_dict[string] < 0:
            return string