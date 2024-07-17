def solution(food):
    answer1=''
    answer2=''
    for i in range(1,len(food)):
        if food[i]==1:
            food[i]=0
        elif food[i]%2==1:
            food[i]//=2
        elif food[i]%2==0:
            food[i]//=2
    answer =food
    for i in range(1,len(food)):
        for j in range(food[i]):
            answer1+=str(i)
    for i in range(len(answer1)-1,-1,-1):
            answer2+=str(answer1[i])
    answer=answer1+'0'+answer2
    return answer
        