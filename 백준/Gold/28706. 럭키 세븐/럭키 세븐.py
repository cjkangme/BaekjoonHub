import sys

input = sys.stdin.readline

def calculate(command, dp_set):
    temp = set()
    for i in range(0, 4, 2):
        oper, num = command[i], command[i+1]
        for operand in dp_set:
            if oper == "+":
                temp.add((operand + int(num)) % 7)
            else:
                temp.add((operand * int(num)) % 7)
    return temp

if __name__=="__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        commands = [list(map(str, input().split())) for _ in range(N)]
        dp_set = set([1]) # 1부터 시작
        for command in commands:
            dp_set = calculate(command, dp_set)
            
        if 0 in dp_set:
            print("LUCKY")
        else:
            print("UNLUCKY")