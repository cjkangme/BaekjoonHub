def is_blank(x, y, devider):
    if devider == 0:
        return False
    
    if x // devider == 1 and y // devider == 1:
        return True
    else:
        return is_blank(x % devider, y % devider, devider//3)

N = int(input())
    
for i in range(N):
    for j in range(N):
        if is_blank(i, j, N//3):
            print(" ", end="")
        else:
            print("*", end="")
    print()