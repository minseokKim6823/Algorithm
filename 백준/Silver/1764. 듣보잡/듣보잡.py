import sys
input=sys.stdin.readline
A,B=map(int,input().split())
dict1= {}
lst2=[]
for i in range(A):
    T=input()
    result =  T.replace("\n", "")
    dict1[result]=0
for i in range(B):
    x=input()
    x = x.replace("\n", "")
    if x in dict1:
        lst2.append(x)
lst2.sort()
print(len(lst2))
for i in range(len(lst2)):
    print(lst2[i])