X, Y = map(int, input().split())
Z = (Y * 100) // X
def bi(left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    newZ = int((Y + mid) / (X + mid) * 100)
    if newZ > Z:
        ans = bi(left, mid - 1)
        if ans == -1:
            return mid
        else:
            return ans
    else:
        return bi(mid + 1, right)
if Z >= 99:
    print(-1)
else:
    print(bi(1, 1000000000))