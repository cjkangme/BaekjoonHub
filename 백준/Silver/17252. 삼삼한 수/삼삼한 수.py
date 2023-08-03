import sys

if __name__=="__main__":
    num = int(input())
    
    if num == 0:
        print("NO")
        sys.exit(0)
    
    digit = 1
    while digit < num:
        digit *= 3
    
    while digit:
        if num >= digit:
            num -= digit
        digit //= 3
    
    print("NO" if num else "YES")