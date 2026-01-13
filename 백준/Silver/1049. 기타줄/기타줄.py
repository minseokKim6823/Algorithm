N, M = map(int,input().split())
result=0
P=9999
T=9999
for i in range(M):
    A,B = map(int,input().split())
    if P>=A:
        P = A
    if T>=B:
        T = B
# N = 끊어진 기타 줄 개수, M = 기타줄 브랜드 갯수
if T*6<=P: #개별이 더 쌀떄
    result = T*N
else: #패키지가 더 쌀떄
    if N<=6:
        result=P
    else:
       Y = N % 6
       if Y*T<=P:
           result+=Y*T
       else:
           result+=P
       result += (N//6)*P
print(result)
