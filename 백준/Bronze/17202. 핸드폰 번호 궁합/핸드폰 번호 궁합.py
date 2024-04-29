A=input()
B=input()
lst1=[]
cnt=0
end=15
for i in range(8):
    lst1.append(A[i])
    lst1.append(B[i])
for i in range(14):
    for j in range(len(lst1)-1):
        lst1[j]=(int(lst1[j])+int(lst1[j+1]))%10
    lst1.pop()
for i in range(2):
    print(lst1[i],end="")



# 74759336
# 36195974