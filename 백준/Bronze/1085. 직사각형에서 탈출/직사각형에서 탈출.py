x,y,w,h=map(int,input().split())
min=9999
for i in range(4):
    if(min>=x):
        min=x
    if(min>=y):
        min=y
    if(min>=w-x):
        min=w-x
    if(min>=h-y):
        min=h-y
print(min)