import sys
n = int(input())
result = [0] * 10001

for _ in range(n) :
    result[int(sys.stdin.readline())] += 1


for idx in range(10001) :
    for n in range(result[idx]):
        print(idx)