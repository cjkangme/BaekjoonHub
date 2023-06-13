import math 
N, M = map(int, input().split())

if N == 1:
    print(1)
elif N == 2:
    print(min(4, math.ceil(M / 2)))
else:
    if M <= 4:
        print(M)
    elif M == 5:
        print(4)
    else:
        print(M-2)