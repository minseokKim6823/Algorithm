list1=[int(i) for i in input().split()]
max=0
for i in range(2):
    b=list1[i]//100
    s=(list1[i]-b*100)//10
    i=list1[i]%10
    su = 100 * i + 10 * s + b
    if(max<su):
        max=su
print(max)
