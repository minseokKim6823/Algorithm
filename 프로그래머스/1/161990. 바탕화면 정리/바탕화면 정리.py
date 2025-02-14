def solution(wallpaper):
    minX=50
    minY=50
    maxX=0
    maxY=0
    answer = [0,0,0,0]
    for y in range(len(wallpaper)):
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x]=='#':
                if minX>=x:
                    minX=x
                if x>=maxX:
                    maxX=x
                if minY>=y:
                    minY=y
                if y>=maxY:
                    maxY=y
        answer[0],answer[1],answer[2],answer[3]=minY,minX,maxY+1,maxX+1
    return answer