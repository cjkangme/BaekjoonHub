import sys

input = sys.stdin.readline

def sum_fomula(fomula):
    return sum(map(int, fomula.split("+")))

# 빼기 기호를 기준으로 분리하여 더하기 식만 남겨둠
fomulas = list(map(str, input().rstrip().split("-")))

answer = sum_fomula(fomulas[0])
for i in range(1, len(fomulas)):
    answer -= sum_fomula(fomulas[i])
    
print(answer)