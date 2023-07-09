import sys

input = sys.stdin.readline

def devide(left, right):
    global hist
    if left == right:
        return hist[left]
    
    mid = (left + right) // 2
    lmid, rmid = mid, mid+1
    area = max(devide(left, lmid), devide(rmid, right))
    
    height = min(hist[lmid], hist[rmid])
    area = max(area, height * 2, hist[lmid], hist[rmid])
    while (left < lmid or rmid < right):
        if (rmid < right and (lmid <= left or (hist[lmid-1] < hist[rmid+1]))):
            rmid += 1
            height = min(height, hist[rmid])
        else:
            lmid -= 1
            height = min(height, hist[lmid])
        area = max(area, height * (rmid-lmid+1))
    return area
    
while True:
    inputs = list(map(int, input().split()))
    if inputs == [0]:
        break
    answer = 0
    n = inputs[0]
    hist = inputs[1:]
    
    print(devide(0, n-1))