list1=[int(i) for i in input().split()]
result=0
for i in range(len(list1)):
    result+=list1[i]**2
print(result%10)