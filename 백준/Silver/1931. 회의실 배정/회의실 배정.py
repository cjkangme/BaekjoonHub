import sys 
input = sys.stdin.readline

answer = 0
time = 0

N = int(input())
meetings = []
for _ in range(N):
    meetings.append(tuple(map(int, input().split())))

meetings.sort(key = lambda x : (x[1], x[0]))

for meeting in meetings:
    start, end = meeting
    
    if start >= time:
        answer += 1
        time = end
        
print(answer)