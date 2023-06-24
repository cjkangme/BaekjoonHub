import sys

input = sys.stdin.readline

# 조각이 모두 같은 수로 이루어져 있는지 판별하는 함수
# 모두 같은수라면 조각의 수 반환, 아니면 100 반환
def is_same(board):
    mark = board[0][0]
    for row in board:
        for cell in row:
            if cell != mark:
                return 100
    return mark

if __name__ == "__main__":
    N = int(input())
    initial_board = [list(map(int, input().split())) for _ in range(N)]
    stack = [initial_board]
    answers = [0, 0, 0] # -1, 0, 1 순서, 저장할 때는 +1하면 인덱스와 일치함
    
    while stack:
        board = stack.pop()
        # 조각이 모두 같은 수가 아니라면 9등분하여 스택에 추가
        mark = is_same(board)
        if mark == 100:
            separator = len(board[0]) // 3
            for x in range(0, len(board), separator):
                separated_boards = [[], [], []]
                temp_board = board[x:x+separator]
                for i in range(separator):
                    for j in range(3):
                        idx = j*separator
                        separated_boards[j].append(temp_board[i][idx:idx+separator])
                for separated_board in separated_boards:
                    stack.append(separated_board)
        # 같은 수라면 답에 조각 추가
        else:
            answers[mark+1] += 1
    # 스택이 비어 while문 탈출 시 답 출력
    for answer in answers:
        print(answer)
            
        