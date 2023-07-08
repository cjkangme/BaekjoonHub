def draw(n):
    if n==1:
        return ["*"]
    
    stars = draw(n//3)
    board = []
    
    for star in stars:
        board.append(star * 3)
    for star in stars:
        board.append(star + " "*(n//3) + star)
    for star in stars:
        board.append(star * 3)
    
    return board

if __name__ == "__main__":
    N = int(input())
    answer = draw(N)
    
    for i in range(N):
        for j in range(N):
            print("".join(answer[i][j]), end="")
        print()