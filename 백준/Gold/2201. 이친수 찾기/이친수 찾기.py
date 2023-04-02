def get_digit(num):
    digit = 0
    curr = 1
    prev = 1
    while curr <= num:
        digit += 1
        curr, prev = curr+prev, curr
    return (digit-1, prev)

K = int(input())

remain = K
answer = 0

while remain:
    digit, curr = get_digit(remain)
    answer += 10 ** digit
    remain -= curr

print(answer)