num = int(input())
lst=[]
lst1=[]
for i in range(num):
    word = input()
    lst.append(word)
word1 = lst[0]
for i in lst:
    if i != word1:
        for j in range(len(word)):
            if i[j] != word1[j]:
                if j not in lst1:
                    lst1.append(j)
result = list(word)
for i in lst1:
    result[i]='?'
result=''.join(result)
print(result)