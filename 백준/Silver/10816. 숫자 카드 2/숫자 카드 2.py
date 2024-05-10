n = int(input())
dic = {}
arr = list(map(int, input().split()))
for item in arr:
    if item not in dic:
        dic[item] = 0
    dic[item]+=1
m = int(input())
ans = []
query = list(map(int, input().split()))
for q in query:
    if q not in dic:
        print(0, end=' ')
    else:
        print(dic[q], end=' ')