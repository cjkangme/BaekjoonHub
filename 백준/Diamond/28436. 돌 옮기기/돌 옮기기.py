import sys

input = sys.stdin.readline

STONE_TO_IDX = {
    "W": 0,
    "B": 1
}

if __name__=="__main__":
    T = int(input())
    
    for _ in range(T):
        stones = input().rstrip()
        
        prev = "." # 이전에 나온 돌을 저장
        cnt = 0 # 연속으로 나온 "."의 횟수를 저장 (돌을 밀 수 있는 횟수)
        move = 0 # W 돌을 B대비 더 많이 움직일 수 있는 횟수
        
        for idx, stone in enumerate(stones[::-1]):
            # 맨 뒤에있는 "." 들을 버리는 부분
            if prev == ".":
                prev = stone
            if prev == ".":
                continue
            
            if stone == ".":
                move += (1 if prev=="W" else -1) * cnt
            elif prev == stone:
                cnt += 1
            else:
                cnt = 0
                prev = "."
                
        print("WHITE" if move > 0 else "BLACK")