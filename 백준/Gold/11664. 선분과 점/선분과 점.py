import sys

MIN_ERROR = 1e-6

def gradient_decent(x, count):
    result = (x - c_x) + dy * (dy*x + cy - c_y) +  dz * (dz*x + cz - c_z)

    # 미분값(result)이 양수면 True, 음수면 False 반환
    if result > 0:
        return True
    return False

def get_distance(x1, x2, y1, y2, z1, z2):
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** 0.5

if __name__=="__main__":
    a_x, a_y, a_z, b_x, b_y, b_z, c_x, c_y, c_z = map(int, input().split())
    count = 0
    if (a_z == b_z):
        count += 1
    if (a_y == b_y):
        count += 1
    if (a_x == b_x):
        count += 1
        if a_z != b_z:
            a_x, b_x, a_z, b_z = a_z, b_z, a_x, b_x
        elif a_y != b_y:
            a_x, b_x, a_y, b_y = a_y, b_y, a_x, b_x
    
    lo, hi = min(a_x, b_x), max(a_x, b_x)
    dx, dy, dz = 1, (b_y-a_y) / (b_x-a_x), (b_z-a_z) / (b_x-a_x)
    cx, cy, cz = 0, a_y - (dy * a_x), a_z - (dz * a_x)
    
    if count == 2:
        print(get_distance(c_x, c_x, (dy*c_x)+cy, c_y, (dz*c_x)+cz, c_z))
        sys.exit(0)
    # x가 최소일때도 미분값이 양수면 최솟값의 점이 가장 가까운 거리 
    if gradient_decent(lo, count):
        print(get_distance(lo, c_x, (dy*lo)+cy, c_y, (dz*lo)+cz, c_z))
        sys.exit(0)
    # x가 최대일때도 미분값이 음수면 최댓값의 점이 가장 가까운 거리
    if not gradient_decent(hi, count):
        print(get_distance(hi, c_x, (dy*hi)+cy, c_y, (dz*hi)+cz, c_z))
        sys.exit(0)
    
    t_x, t_y, t_z = a_x, a_y, a_z
    lo, hi = min(a_x, b_x), max(a_x, b_x)
    while lo <= hi:
        mid = (lo + hi) / 2
        if gradient_decent(mid, count):
            hi = mid - MIN_ERROR
        else:
            lo = mid + MIN_ERROR
     
    print(get_distance(hi, c_x, (dy*hi)+cy, c_y, (dz*hi)+cz, c_z)) 