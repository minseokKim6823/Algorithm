lst=[0,"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
N= int(input())
M= input()
result=0
cnt=0
for i in range(len(M)):
    result+=lst.index(M[i])*31**cnt
    cnt+=1
print(result)