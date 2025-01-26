def solution(park, routes):
    answer=[0,0]
    h=len(park)-1
    w=len(park[0])-1
    r=len(routes)
    for i in range(h+1):
        for j in range(w+1):
            if park[i][j]=='S':
                answer=[i,j]
    y=answer[0]
    x=answer[1]
    print(y,x)
    for i in range(r):
        x1=0
        y1=0
        if routes[i][0]=="E":
            for j in range(int(routes[i][2])):
                x1+=1
                if x+x1>w:
                    x1=0
                    break
                elif park[y][x+x1]=='X':
                    x1=0    
                    break
            x+=x1
        elif routes[i][0]=="W":
            for j in range(int(routes[i][2])):
                x1+=1
                if x-x1<0:
                    x1=0
                    break
                elif park[y][x-x1]=='X':
                    x1=0
                    break
            x-=x1
        elif routes[i][0]=="S":
            for j in range(int(routes[i][2])):
                y1+=1
                if y+y1>h:
                    y1=0
                    break
                elif park[y+y1][x]=='X':
                    y1=0
                    break
            y+=y1
        elif routes[i][0]=="N":
            for j in range(int(routes[i][2])):
                y1+=1
                if y-y1<0:
                    y1=0
                    break
                elif park[y-y1][x]=='X':
                    y1=0
                    break
            y-=y1
    answer=[y,x]
    
    return answer