# 1, 2, 3, 4 분면일때 각각 곱해주어야 하는 값
dx = [0, 0, 0, 1, 1]
dy = [0, 1, 0, 0, 1]

if __name__ == "__main__":
    d, num = map(int, input().split())
    move_y, move_x = map(int, input().split())
    
    # 최대 좌표 설정
    max_x, max_y = 2 ** d, 2 ** d
    x, y = 0, 0
    
    # 처음 주어진 사분면 조각의 위치 찾기
    for idx, str_digit in enumerate(str(num)):
        digit = int(str_digit)
        x += dx[digit] * (2 ** (d-idx-1))
        y += dy[digit] * (2 ** (d-idx-1))
    # 이동할 좌표만큼 더하기
    x -= move_x
    y += move_y
    # 존재하지 않는 사분면이면 -1 출력
    if x >= max_x or x < 0 or y >= max_y or y < 0:
        print(-1)
    else:
        # 좌표를 바탕으로 사분면 번호 구하기
        answer = ""
        for idx in range(1, d+1):
            digit = 2
            criteria = 2 ** (d-idx)
            # (1 -> 3), (2 -> 4) or 그대로
            if x >= criteria:
                x -= criteria
                digit += 2
            # 그대로 or (2 -> 1), (4 -> 3)    
            if y >= criteria:
                y -= criteria
                if digit == 2:
                    digit -= 1
            else:
                if digit == 4:
                    digit -= 1

            answer += str(digit)
        print(answer)