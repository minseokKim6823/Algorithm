t=2
lst=[t*t]
N=int(input())
for i in range(N):
    t= t*2-1
    lst.append(t**2)

print(lst[N])