def solution(dots):
    answer=0
    dot1=dots[0]
    for i in range(1,4):
        list1=[1,2,3]
        dot2=dots[i]
        list1.remove(i)
        x1=abs(dot1[0]-dot2[0])
        y1=abs(dot1[1]-dot2[1])
        x2=abs(dots[list1[0]][0]-dots[list1[1]][0])
        y2=abs(dots[list1[0]][1]-dots[list1[1]][1])
        if y1/x1==y2/x2:
            answer=1
        
    return answer