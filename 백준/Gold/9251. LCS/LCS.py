if __name__=="__main__":
    str_A = input()
    str_B = input()
    board = [[0] * (len(str_A) + 1) for _ in range(2)]
    
    for i, char_B in enumerate(str_B):
        idx = i % 2
        idx_ref = idx - 1
        for j, char_A in enumerate(str_A):
            if char_A == char_B: 
                board[idx][j+1] = board[idx_ref][j] + 1
            else:
                board[idx][j+1] = max(board[idx_ref][j+1], board[idx][j])
   
    print(board[idx][-1])
