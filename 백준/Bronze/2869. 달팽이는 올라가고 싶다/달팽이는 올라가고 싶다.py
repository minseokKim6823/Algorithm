A,B,V=map(int,input().split())
cnt=0
cicle=A-B
if((V-A)%cicle!=0):
    print(((V-A)//cicle)+2)
else:
    print(((V - A) // cicle)+1)