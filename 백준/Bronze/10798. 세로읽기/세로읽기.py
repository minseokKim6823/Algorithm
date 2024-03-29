list1=[]
list2=[]
list3=[]
min=0
for q in range(5):
    list1.append(list(input()))
    list2.append(len(list1[q]))
length=max(list2)
for i in range(5):
    if len(list1[i])<length:
        while len(list1[i])!=length:
            list1[i].append('')

for i in range(length):
    for j in range(5):
        if(list1[j][i]!=''):
            list3.append(list1[j][i])

for i in range(len(list3)):
    print(list3[i],end='')