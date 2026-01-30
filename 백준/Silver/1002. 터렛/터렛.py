import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    d = dx*dx + dy*dy          
    sum_r = (r1 + r2) ** 2
    diff_r = (r1 - r2) ** 2

    if dx == 0 and dy == 0 and r1 == r2:
        print(-1)             
    elif d > sum_r:
        print(0)               
    elif d < diff_r:
        print(0)               
    elif d == sum_r:
        print(1)               
    elif d == diff_r:
        print(1)               
    else:
        print(2)   