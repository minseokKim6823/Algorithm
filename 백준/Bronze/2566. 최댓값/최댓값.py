list1=[]
result=0

for _ in range(9):
    list1.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if list1[i][j] >= result:
            result=list1[i][j]
            r=i+1
            c=j+1

print(result)
print(r, c)