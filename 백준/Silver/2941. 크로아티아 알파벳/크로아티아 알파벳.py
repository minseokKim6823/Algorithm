list1=['c=','c-','dz=','d-','lj','nj','s=','z=']
word=input()
skip=0
result=0
#print(len(word))
for i in range(len(word)):
    #print("i=",i)
    #print("skip=",skip)
    if i<=len(word)-3 and word[i]+word[i+1]+word[i+2] in list1 and skip==0:
        skip=2
        result+=1
        #print("1번")
    elif i <= len(word) - 2 and word[i]+word[i+1] in list1 and skip==0:
        skip = 1
        result += 1
        #print("2번")
    elif skip==0 :
        result+=1
        #print("3번")
    else:
        skip-=1
        #print("4번")
print(result)
