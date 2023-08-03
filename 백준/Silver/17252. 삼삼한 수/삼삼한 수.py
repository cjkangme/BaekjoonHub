def bit_to_num(bits):
    digit = 1
    num = 0
    
    while bits:
        if bits & 1:
            num += digit
        bits = bits >> 1
        digit *= 3
    
    return num
        

if __name__=="__main__":
    N = int(input())
    flag = False
    temp = N
    digit = 0
    
    while temp >= 3:
        temp //= 3
        digit += 1 
    
    # 비트마스크
    for bits in range(1, 2 ** (digit+1)):
        num = bit_to_num(bits)
        if num == N:
            flag = True
            break
        elif num > N:
            break
    
    print("YES" if flag else "NO")  