N, M = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(N)]
T=False
s = N
if M<N:
    s=M
for i in range(s-1,0,-1):
    for x in range(M-i):
        for y in range(N-i):
            if arr[y][x] == arr[y+i][x] and arr[y][x] == arr[y][x+i] and arr[y][x] == arr[y+i][x+i]:
                print((i+1)**2)
                T=True
                exit(0)
if T==False:
    print(1)

