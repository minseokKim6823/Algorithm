list1=[[65,66,67],[68,69,70],
       [71,72,73],[74,75,76],
       [77,78,79],[80,81,82,83],
       [84,85,86],[86,87,88,89]]
result=0
word=input()
for i in range(len(word)):
    if ord(word[i]) in list1[0]:
        result+=3
    elif ord(word[i]) in list1[1]:
        result+=4
    elif ord(word[i]) in list1[2]:
        result+=5
    elif ord(word[i]) in list1[3]:
        result+=6
    elif ord(word[i]) in list1[4]:
        result+=7
    elif ord(word[i]) in list1[5]:
        result+=8
    elif ord(word[i]) in list1[6]:
        result+=9
    else:
        result+=10
print(result)