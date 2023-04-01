num=int(input())
num-=1
for i in range(num):
    for k in range(num-i,0,-1):
        print(" ",end="")
        num1=i*2+1
    print("*"*num1)
for i in range(num*2+1):
    print("*",end="")
print("")
for i in range(1,num+1):
    for k in range(i):
        print(" ",end="")
        num2=(num*2+1)-2*i
    print("*"*num2)