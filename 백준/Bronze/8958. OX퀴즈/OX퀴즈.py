su=int(input())
cnt=0
s=1
for i in range(su):
    sum=0
    b = []
    a=input()
    s = 1
    for i in range(len(a)):
        if a[i]== 'O':
            sum+=s
            s+=1
        elif a[i]== 'X':
            s=1
    print(sum)

