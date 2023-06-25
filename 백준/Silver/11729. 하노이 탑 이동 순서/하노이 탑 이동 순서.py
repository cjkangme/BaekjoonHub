# start에 있는 n번 원판을 target으로 옮기는 함수
def move_hanoi(n, start, target, remain):
    # 1번 원판이라면 즉시 target으로 옮기고 종료
    if n == 1:
        answers.append((start+1, target+1))
        answers[0] += 1
        return
    # 아니라면 위에있는 n-1번 원판을 remain으로 치워야 함
    move_hanoi(n-1, start, remain, target)
    
    # 위 과정을 거쳤다면 n번 원판을 target으로 옮길 수 있음
    answers.append((start+1, target+1))
    answers[0] += 1
    
    # 이제 remain에 남아있는 n-1번 원판을 target으로 가져옴
    move_hanoi(n-1, remain, target, start)

N = int(input())
answers = [0]

move_hanoi(N, 0, 2, 1)

print(answers[0])
[print(*answer) for answer in answers[1:]]