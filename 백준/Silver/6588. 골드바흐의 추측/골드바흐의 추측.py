import sys
input = sys.stdin.readline

MAX_NUM = 1000000

prime_list = list(range(MAX_NUM+1))
for i in range(2, 1001):
    if prime_list[i]:
        prime_list[i+i::i] = [0] * len(prime_list[i+i::i])

prime_list = list(filter(None, prime_list[2:]))
prime_set = set(prime_list)

while n := int(input()):
    for a in prime_list:
        b = n - a
        if b in prime_set:
            print(f'{n} = {a} + {b}')
            break
    else:
        print("Goldbach's conjecture is wrong.")
