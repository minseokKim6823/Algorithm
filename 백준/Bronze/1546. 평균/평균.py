num=int(input())
sum=0
list1=[int(i) for i in input().split()]
max=max(list1)
for i in range(len(list1)):
    list1[i]/=max
    sum+=list1[i]
print(sum/len(list1)*100)
