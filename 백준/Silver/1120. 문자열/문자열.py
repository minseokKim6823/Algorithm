A,B = map(str,input().split())
if len(A) == len(B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    print(cnt)
else:
    min = 9999
    for c in range(len(B)-len(A)+1):
        cnt = 0
        for i in range(len(A)):
            if A[i] != B[i+c]:
                cnt += 1
        if min > cnt:
            min = cnt
        if min ==0:
            print(0)
            exit()
    print(min)
# for i in range(1,3): #1,2
#     print(i)