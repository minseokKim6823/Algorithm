N, m, M, T, R = map(int,input().split())
# 초기맥박 = m, 증가 맥박 =T, 감소 맥박 =R, 최대 맥박=M
workout = 0
time=0
pulse=m
if m+T>M:
    print(-1)
    exit(0)

while workout != N:
    if pulse+T <= M:
        pulse += T
        workout += 1
    else:
        pulse -= R
        if pulse < m:
            pulse = m
    time += 1
print(time)