import sys
from itertools import combinations

input = sys.stdin.readline

def word2bit(word):
    bit = 0
    for char in word:
        bit = bit | (1 << ord(char) - ord('a'))
    return bit

N, K = map(int, input().split())
words = [input().rstrip() for _ in range(N)]
bits = list(map(word2bit, words))
base_word = word2bit('antic')

if K < 5:
    print(0)
else:
    alphabet = set([chr(i) for i in range(ord('a'), ord('z')+1)])
    alphabet = alphabet - set(['a', 'n', 't', 'i', 'c'])
    answer = 0
    for combination in combinations(alphabet, K-5):
        know_word = list(combination)
        know_bit = base_word | word2bit(know_word)
        count = 0
        for bit in bits:
            if bit & know_bit == bit:
                count += 1
        answer = max(answer, count)
    print(answer)