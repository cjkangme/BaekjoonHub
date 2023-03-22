import sys

DEVIDER = 1000000

password = list(map(int, input()))

length = len(password)

dy = [[0, 0] for _ in range(length)]
# 앞자리를 활용한 경우, 앞자리를 활용하지 않은 경우
if password[0] == 0:
    dy[0] = [0, 0] # 첫글자가 0이면 무조건 잘못된 암호
else:
    dy[0] = [0, 1]

for i in range(1, length):
    case = password[i-1] * 10 + password[i]
    if password[i] == 0:
        dy[i][1] = 0    # 앞자리를 무조건 활용해야 함
    else:
        dy[i][1] = (dy[i-1][0] + dy[i-1][1]) % DEVIDER
        
    # 앞자리를 활용할 수 있는 경우
    if 0 < case <= 26:
        dy[i][0] = dy[i-1][1]
    
    # 암호가 잘못되어 해석할 수 없는 경우
    if dy[i] == [0, 0]:
        print(0)
        sys.exit(0)
        
print(sum(dy[-1]) % DEVIDER)