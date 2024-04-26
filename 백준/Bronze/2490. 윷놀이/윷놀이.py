lst1=[]
lst2=[]
for j in range(3):
    A, B, C, D = map(int, input().split())
    cnt = 0
    if A == 0:
        cnt += 1
    if B == 0:
        cnt += 1
    if C == 0:
        cnt += 1
    if D == 0:
        cnt += 1
    lst1.append(cnt)
for i in range(len(lst1)):
    if lst1[i]==1:
        lst2.append('A')
    if lst1[i]==2:
        lst2.append('B')
    if lst1[i]==3:
        lst2.append('C')
    if lst1[i]==4:
        lst2.append('D')
    if lst1[i]==0:
        lst2.append('E')
for i in range(3):
    print(lst2[i])