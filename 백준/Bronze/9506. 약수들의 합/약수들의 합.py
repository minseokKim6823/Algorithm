n=0
while n!=-1:
    lst = []
    n=int(input())
    if n== -1:
        break
    for i in range(1,n//2+1):
        if(n%i==0):
            lst.append(i)
    if sum(lst)==n:
        print(n,end=" = ")
        for i in range(len(lst) - 1):
            print(lst[i] , end=" + ")
        print(lst[len(lst)-1])
    else:
        print(n,"is NOT perfect.")

