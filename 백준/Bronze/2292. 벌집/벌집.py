N = int(input())

def get_room(cnt):
    max_room = 3 * (cnt ** 2) - (3 * cnt) + 1
    min_room = max_room - ((cnt - 1) * 6)
    return max_room, min_room

def search(left, right):
    pivot = (left + right) // 2
    if pivot == 1:
        return search(1, 3)
    max_room, min_room = get_room(pivot)
    if N > min_room and N <= max_room:
        return pivot
    elif N > max_room:
        left = pivot
        while(right <= left):
            right += 1
        return search(left, right)
    else:
        right = pivot
        while(left >= right):
            left -=1
        return search(left, right)
if N == 1:
    print(1)
else:
    print(search(1,18260))