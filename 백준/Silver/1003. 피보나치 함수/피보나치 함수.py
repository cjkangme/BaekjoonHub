import sys

input = sys.stdin.readline
MAX_N = 41

def make_solution_array():
    solution_array = [[0] * 2 for _ in range(MAX_N)]
    solution_array[0] = [1, 0]
    solution_array[1] = [0, 1]
    
    for i in range(2, MAX_N):
        solution_array[i][0] = solution_array[i-1][0] + solution_array[i-2][0]
        solution_array[i][1] = solution_array[i-1][1] + solution_array[i-2][1]
    return solution_array

if __name__ == "__main__":
    T = int(input())
    solution_array = make_solution_array()
    for _ in range(T):
        N = int(input())
        
        print(*solution_array[N])
    
    