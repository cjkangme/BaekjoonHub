from collections import deque

if __name__ == "__main__":
    N = int(input())
    # i번 수가 로마숫자를 통해 표현할 수 있는지 여부
    arr = [0]
    # 브루트포스
    for _ in range(N):
        temp = []
        numbers = set()
        count = 0
        for num in arr:
            for add in [1, 5, 10, 50]:
                next_num = num + add
                if next_num in numbers:
                    continue
                temp.append(next_num)
                numbers.add(next_num)
                count += 1
        arr = temp
    print(count)