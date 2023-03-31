import sys
input = sys.stdin.readline

if __name__=="__main__":
    n = int(input())
    wine = []
    for _ in range(n):
        wine.append(int(input()))
    while len(wine) < 3:
        wine.append(0)
    dy = [0 for _ in range(n+2)]
    dy[0] = wine[0]
    dy[1] = wine[0] + wine[1]
    dy[2] = max(wine[0]+wine[2], dy[1], wine[1]+wine[2])
    for i in range(3, n):
        dy[i] = max(dy[i-1], dy[i-2]+wine[i], dy[i-3]+wine[i]+wine[i-1])
    print(max(dy))