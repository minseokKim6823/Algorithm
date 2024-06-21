def solution(n, control):
    for i in range(len(control)):
        if control[i]=='w':
            n+=1
        elif control[i]=='s':
            n-=1
        elif control[i]=='d':
             n+=10
        else:
            n-=10
    answer = n
    return answer