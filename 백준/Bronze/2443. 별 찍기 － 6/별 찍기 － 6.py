num=int(input())
t=num*2-1
for i in range(num):
    print(" "*i,end="")
    print("*"*(t-(2*i)))