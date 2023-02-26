def devide(x, y):
    if x % y == 0:
        return x // y
    else:
        return (x // y) + 1


if __name__ == "__main__":
    A, B, X, Y, Z = map(int, input().split())
    total_credit = Y * Z
    prod = [[0] * 2 for _ in range(100001)]
    answer = 2147000000
    prod[B][1] = A
    for i in range(B+1, Y+1):
        upgrade_day = devide(X-prod[i-1][1], i-1)
        prod[i][0] = max(prod[i-1][0] + max(devide(X-prod[i-1][1], i-1), 1), (i-B))
        prod[i][1] = max(prod[i-1][1] + (prod[i][0] -
                         prod[i-1][0]) * (i-1) - X, 0)
    for j in range(min(B, Y), Y+1):
        answer = min(answer,  max(
            prod[j][0] + devide((total_credit - prod[j][1]), j), Z))

    print(answer)