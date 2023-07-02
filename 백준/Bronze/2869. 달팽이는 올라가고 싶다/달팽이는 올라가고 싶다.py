import sys
input = sys.stdin.readline

A,B,V = map(int,input().split())
height = V - A
climb = A - B
if climb == 1 or height == 0:
    print(height + 1)
elif (height % climb) == 0:
    print((height // climb) + 1)
else:
    print((height // climb) + 2)
