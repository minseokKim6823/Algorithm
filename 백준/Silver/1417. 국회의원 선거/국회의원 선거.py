list1=[]
result=0
num=int(input())
for i in range(num):
    su=int(input())
    list1.append(su)
t = list1[0]
if len(list1)==1:
    pass
elif max(list1)<t:
    pass
else:
    del list1[0]
    while t<=max(list1):
        max2 = max(list1)
        if (max2 < t):
            break
        else:
            q = list1.index(max2)
            temp=max2-1
            t+=1
            result+=1
            list1[q]=list1[q]-1
print(result)