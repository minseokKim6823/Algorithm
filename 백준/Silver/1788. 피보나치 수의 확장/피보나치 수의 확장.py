T = int(input())
if T==0:
    print(0)
    print(0)
    exit()
if(T == 1 or T == -1):
    print(1)
    print(1)
    exit()
result = 0
A = 0
B = 1
F = abs(T)
for i in range(F-1):
    temp = B
    result = A + B
    B = result
    A = temp
if T < 0 and (T*-1) % 2 == 0:
    print(-1)
    print(result % 1000000000)
else:
    print(1)
    print(result % 1000000000)