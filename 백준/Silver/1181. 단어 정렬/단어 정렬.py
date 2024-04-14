N=int(input())
lst=[]
for i in range(20000):
    lst.append([])
for i in range(N):
    word=str(input())
    cnt=len(word)
    if word not in lst[cnt]:
        lst[cnt].append(word)
for i in range(20000):
    lst[i].sort()
for i in range(20000):
    for j in range(len(lst[i])):
        print(lst[i][j])