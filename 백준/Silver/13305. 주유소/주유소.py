N= int(input())
lst1 = [int(i) for i in input().split()]
#다음 주유소 까지 거리
lst2 = [int(i) for i in input().split()]
#가격
result=0
min=lst2[0]
for i in range(N-1):
    if min>lst2[i]:
        min=lst2[i]
    result += min*lst1[i]
print(result)
