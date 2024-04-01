word='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst1=[]
lst2=[]
N,B=map(int,input().split())
V=0
while N>=B:
    V=N%B
    N=N//B
    lst1.append(V)
lst1.append(N)

for i in range(len(lst1)-1,-1,-1):
    lst2.append(word[lst1[i]])
    print(word[lst1[i]],end="")
