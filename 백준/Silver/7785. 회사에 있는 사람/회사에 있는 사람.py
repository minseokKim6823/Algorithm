import sys
input=sys.stdin.readline
dic={}
N=int(input())
for i in range(N):
    A,B=map(str,input().split())
    dic[A]=B
    if B=="leave":
        del dic[A]
dic=sorted(dic,reverse=True)
for i in dic:
    print(i)
'''
4
Baha enter
Bskar enter
Baha leave
Artem enter
'''