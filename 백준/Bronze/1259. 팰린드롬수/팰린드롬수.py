num=1
while num!=0:
    result="yes"
    cnt=0
    num=str(input())
    if(num=="0"):
        break
    for i in range(len(num)-1,-1,-1):
        if num[i]!=num[cnt]:
            result ="no"
        cnt+=1

    print(result)


