import sys
from itertools import combinations

input = sys.stdin.readline

def get_count(words, known, max_count):
    count = 0
    for idx, word in enumerate(words):
        if N - idx + count <= max_count:
            return count
        for char in word:
            if char not in known:
                break
        else:
            count += 1
    return count

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
base = set(['a', 'n', 't', 'i', 'c'])
answer = 0
if K < 5:
    print(0)
else:
    alphabet = set([chr(i) for i in range(ord('a'), ord('z')+1)])
    alphabet = alphabet - base
    for combination in combinations(alphabet, K-5):
        temp = set(combination) | base
        answer = max(answer, get_count(words, temp, answer))
    print(answer)