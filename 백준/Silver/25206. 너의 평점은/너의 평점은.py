list1=["A+","A0","B+","B0","C+","C0","D+","D0","F","P"]
list2=[4.5,4.0,3.5,3.0,2.5,2.0,1.5,1.0,0,0]
sum1=0
sum=0
for i in range(20):
    A,B,C= map(str, input().split())
    if C=="P":
        continue
    else:
        sum1= sum1 + float(B) * float(list2[list1.index(C)])
        sum = sum + float(B)
print(sum1/sum)