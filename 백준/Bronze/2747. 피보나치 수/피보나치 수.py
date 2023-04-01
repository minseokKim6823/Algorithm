num=int(input())
n_2=0
n_1=1
for i in range(num-1):
    n=n_2+n_1
    result=n
    temp=n_1
    n_2=temp
    n_1=n
if(num==1):
    result=1
print(result)