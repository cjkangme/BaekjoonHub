import sys
import math

input = sys.stdin.readline

def insert(hq, num):
    index = len(hq)
    hq.append(num)
    
    # 처음 삽입하는 배열이면 교체 필요 없음
    if index == 0:
        return hq
    
    parent = math.ceil(index / 2) - 1
    while True:
        # 부모가 자식보다 크면 교체, 아니면 탈출
        if hq[parent] > hq[index]:
            hq[parent], hq[index] = hq[index], hq[parent]
            index = parent
            parent = math.ceil(index / 2) - 1
            # 루트까지 도달하면 탈출
            if index == 0:
                break
        else:
            break
    return hq

def pop(hq):
    if len(hq) > 0:
        print(hq[0])
        hq[0] = hq[-1]
        hq.pop()
        index = 0
        length = len(hq)
        while True:
            left, right = index * 2 + 1, index * 2 + 2
            if left >= length and right >= length:
                break
            elif right >= length:
                if hq[index] > hq[left]:
                    hq[index], hq[left] = hq[left], hq[index]
                break
            else:
                flag = hq[left] > hq[right]
                if flag:
                    if hq[index] > hq[right]:
                        hq[index], hq[right] = hq[right], hq[index]
                        index = right
                    else:
                        break
                else:
                    if hq[index] > hq[left]:
                        hq[index], hq[left] = hq[left], hq[index]
                        index = left
                    else:
                        break
        return hq
    else:
        print(0)
        return hq
    
if __name__=="__main__":
    N = int(input())
    hq = []
    for _ in range(N):
        x = int(input())
        
        if x > 0:
            hq = insert(hq, x)
        else:
            hq = pop(hq)