X = int(input())
lst=[64,32,16,8,4,2]
cnt = 0
if X%2==1:
    X-=1
    cnt+=1
while X!=0:
    if X >= lst[0]:
        cnt += X // lst[0]
        X = X % lst[0]
    elif X >= lst[1]:
        cnt += X // lst[1]
        X = X % lst[1]
    elif X >= lst[2]:
        cnt += X // lst[2]
        X = X % lst[2]
    elif X >= lst[3]:
        cnt += X // lst[3]
        X = X % lst[3]
    elif X >= lst[4]:
        cnt += X // lst[4]
        X = X % lst[4]
    elif X >= lst[5]:
        cnt += X // lst[5]
        X = X % lst[5]
print(cnt)