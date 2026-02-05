def solve(x, y):
    if x == 0 and y == 0:
        return 1

    k = max(abs(x), abs(y), abs(x + y))
    start = 3 * k * (k - 1) + 2

    if x + y == k and x >= 0: 
        idx = (k - 1) - x
    elif y == k: 
        idx = k + (-x - 1)
    elif x == -k:  
        idx = 2 * k + (k - 1 - y)
    elif x + y == -k: 
        idx = 4 * k - 1 + x
    elif y == -k: 
        idx = 4 * k + (x - 1)
    else: 
        idx = 6 * k - 1 + y

    return start + idx


x, y = map(int, input().split())
print(solve(x, y))