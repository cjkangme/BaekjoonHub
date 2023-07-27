def solution(a, b, c):
    numerator_1 = -b
    numerator_2 = int(((b ** 2) - (4 * a * c)) ** 0.5)
    denominator = 2 * a
    
    return ((numerator_1 - numerator_2) // denominator,
            (numerator_1 + numerator_2) // denominator)

if __name__ == "__main__":
    A, B = map(int, input().split())
    
    answer = solution(1, 2*A, B)
    if answer[0] == answer[1]:
        print(answer[0])
    else:
        print(*answer)