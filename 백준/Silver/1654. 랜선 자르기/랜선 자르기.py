import sys

input = sys.stdin.readline


def search(start, end, K, lst1):
    while start <= end:
        mid = (start + end) // 2
        T = sum(cable // mid for cable in lst1)

        if T >= K:
            start = mid + 1
        else:
            end = mid - 1

    return end


N, K = map(int, input().split())
lst1 = [int(input()) for _ in range(N)]

print(search(1, max(lst1), K, lst1))