def binary_search(lo, hi, c):
    while lo < hi:
        mid = round((lo+hi) / 2, 6)
        
        h1 = round((x ** 2 - mid ** 2) ** 0.5, 6)
        h2 = round((y ** 2 - mid ** 2) ** 0.5, 6)
        temp = round((h1 * h2) / (h1 + h2), 6)

        if temp > c:
            lo = mid + 0.000001
        elif temp < c:
            hi = mid - 0.000001
        else:
            return mid
    return hi

x, y, c = map(float, input().split())

max_w = min(x, y)

print(binary_search(0, max_w, c))