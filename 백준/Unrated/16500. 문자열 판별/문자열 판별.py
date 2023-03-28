import sys
from collections import defaultdict

input = sys.stdin.readline

string = input().rstrip()
N = int(input())
words = []
for _ in range(N):
    words.append(input().rstrip())
    
total_len = len(string)
dp = [0] * (total_len+1)
dp[0] = 1

for i in range(total_len):
    if not dp[i]:
        continue
    for word in words:
        length = len(word)
        if word == string[i : i+length]:
            dp[i+length] = 1
    if dp[-1] == 1:
        print(1)
        sys.exit(0)
        
print(0)