import sys
input=sys.stdin.readline
_dict1={}
lst1=[]
A,B=map(int,input().split())
for i in range(A):
    C,D=map(str,input().split())
    _dict1[C]=D
for i in range(B):
    S=input()
    S=S.replace("\n","")
    lst1.append(_dict1[S])
for i in range(len(lst1)):
    print(lst1[i])