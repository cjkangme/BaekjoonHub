import sys

input = sys.stdin.readline

def is_repeated(num):
    exists = set()
    
    while num:
        temp = num % 10
        if temp in exists:
            return False
        exists.add(temp)
        num //= 10
        
    return True


if __name__=="__main__":
    norepeated_list = [0]
    length, num = 1, 1
    while length <= 1000001:
        if is_repeated(num):
            norepeated_list.append(num)
            length += 1
        num += 1

    while idx := int(input()):
        print(norepeated_list[idx])