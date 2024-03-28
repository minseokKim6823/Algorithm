word =input()
result=1
t=0
for i in range(len(word)-1,-1,-1):
    if word[i]==word[t]:
        t+=1
    else:
        result=0
print(result)
