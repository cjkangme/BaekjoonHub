import sys

input = sys.stdin.readline
INF = 2147000000

def calculate_score(before, after):
    if before == 0:
        return 2
    if before == after:
        return 1
    if (before-after) % 2:
        return 3
    return 4

if __name__ == "__main__":
    notes = list(map(int, input().split()))
    N = len(notes)
    # [왼발][오른발]일 때 사용한 힘의 최솟값 5*5*2 3차원 리스트
    dt = [[[INF] * 5 for _ in range(5)] for _ in range(2)]
    deck = []
    
    dt[0][0][notes[0]] = 2
    deck.append((0, notes[0]))
    dt[0][notes[0]][0] = 2
    deck.append((notes[0], 0))
    
    for i in range(1, N-1):
        idx = i % 2
        temp = []
        
        while deck:
            left, right = deck.pop()
            
            # 왼발 옮기기, 같은 칸에 두발이 올 수 없으므로 체크
            if right != notes[i]:
                next_score = dt[idx-1][left][right] + calculate_score(left, notes[i])
                if next_score < dt[idx][notes[i]][right]:
                    dt[idx][notes[i]][right] = next_score
                    temp.append((notes[i], right))
            # 오른발 옮기기
            if left != notes[i]:
                next_score = dt[idx-1][left][right] + calculate_score(right, notes[i])
                if next_score < dt[idx][left][notes[i]]:
                    dt[idx][left][notes[i]] = next_score
                    temp.append((left, notes[i]))
        # 다음에 탐색할 리스트 설정, dt 초기화
        deck = temp
        dt[idx-1] = [[INF] * 5 for _ in range(5)]
    
    # 다이나믹 테이블에서 최솟값 찾아 출력
    if N == 1:
        print(0)
    else:
        print(min(map(min, dt[N % 2])))
