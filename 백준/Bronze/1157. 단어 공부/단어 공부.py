word=(input())
word=word.lower()
cnt=0
list1=[]
list2=[0 for i in range(len(word))]
for i in range(len(word)):
    if word[i] in list1:
        t=list1.index(word[i])
        list2[t]+=1
    else:
        list1.append(word[i])
max1=list2.index(max(list2))
for i in range(len(list2)):
    if list2[i]==list2[max1]:
        cnt+=1
if cnt==1:
    print(list1[max1].upper())
else:
    print('?')

