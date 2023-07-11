def solution(A, power):
    if power == 1:
        return A % C
    
    temp = solution(A, power//2)
    # 홀수인 경우
    if power % 2:
        return (temp * temp * A) % C
    # 짝수인 경우
    else:
        return (temp * temp) % C

if __name__=="__main__":
    A, B, C = map(int, input().split())
    
    print(solution(A, B))