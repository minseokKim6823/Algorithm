N=int(input())
F=int(input())
T=-1
N=N//100*100
while True:
    if N%F==0:
        break
    N+=1
N=str(N)
print(N[len(N)-2],end="")
print(N[len(N)-1])
