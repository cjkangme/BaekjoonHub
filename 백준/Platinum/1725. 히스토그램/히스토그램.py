import sys

input = sys.stdin.readline

def solution(left, right):
    if left == right:
        return hist[left]
    
    mid = (left + right) // 2
    lmid, rmid = mid, mid+1
    area = max(solution(left, lmid), solution(rmid, right))
    
    height = min(hist[lmid], hist[rmid])
    area = max(area, height * 2, hist[lmid], hist[rmid])
    
    while lmid > left or rmid < right:
        if rmid < right and (lmid <= left or hist[rmid+1] > hist[lmid-1]):
            rmid += 1
            height = min(height, hist[rmid])
        else:
            lmid -= 1
            height = min(height, hist[lmid])
        area = max(area, (rmid-lmid+1) * height)

    return area
    

if __name__=="__main__":
    N = int(input())
    hist = [int(input()) for _ in range(N)]
    
    print(solution(0, N-1))