W,H=map(int,input().split())
w,h=map(int,input().split())
t=int(input())
x=1
y=1
a=0
cnt=0
#w계산

X=t%(2*W)
for i in range(X):
    if(w==W):
        x=-1
    elif(w==0):
        x=1
    w+=x
#h계산
Y=t%(2*H)
for i in range(Y): 
    if(h==H):
        y=-1
    elif(h==0):
        y=1
    h+=y
print(w,h)