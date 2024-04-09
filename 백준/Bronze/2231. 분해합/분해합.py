N=int(input())
lst=[]
for i in range(N):
    result=i
    t=str(i)
    for j in range(len(t)):
        result=result+int(t[j])
    if(result==N):
        lst.append(i)
if len(lst)>0:
    print(lst[0])
else:
    print(0)