test=int(input())
list1=[]
for i in range(test):
    floor,room,cnt=map(int,input().split())
    if(floor*room==cnt):
        print(100*floor+room)
    else:
        if(cnt/floor==int(cnt/floor)):
            x=cnt//floor
        else:
            x=cnt / floor+1
        if cnt%floor==0:
            y=floor
        else:
            y=cnt%floor
        print(int(100*y+x))