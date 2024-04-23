lst=["black","brown","red","orange","yellow","green","blue","violet","grey","white"]
for i in range(3):
    t=input()
    t=lst.index(t)
    if i==0:
        result=t*10
    elif i==1:
        result+=t
    elif i==2:
        t=10**t
        result*=t
print(result)
