import sys

input = sys.stdin.readline
pokedex_list = []
pokedex_dict = dict()

def get_answer(question):
    try:
        number = int(question) - 1
        return pokedex_list[number]
    except:
        return pokedex_dict[question]

if __name__ == "__main__":
    N, M = map(int, input().split())
    
    for i in range(1, N+1):
        name = input().rstrip()
        pokedex_list.append(name)
        pokedex_dict[name] = i
        
    for _ in range(M):
        question = input().rstrip()
        print(get_answer(question))