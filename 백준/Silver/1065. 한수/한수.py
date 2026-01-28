N=input()
if int(N)<=99:
    cnt=N
else:
    cnt=99
    for i in range(100,int(N)+1):
        i=str(i)
        if int(i[1])-int(i[0]) == int(i[2])-int(i[1]):
            cnt+=1
print(cnt)
