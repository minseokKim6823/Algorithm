def solution(bandage, health, attacks):
    full_health=health
    cnt=0
    end=False
    l=attacks[len(attacks)-1][0]
    for i in range(1,l):
        if attacks[0][0]==i:
            health-=attacks[0][1]
            del attacks[0]
            if health<0:
                end=True
            cnt=0
        else:
            health+=bandage[1]
            cnt+=1
            if cnt==bandage[0]:
                health+=bandage[2]
                cnt=0
            if health>full_health:
                health =full_health
    for i in attacks:
        health-=i[1]
    if health<=0:
        health=-1
    answer = health
    if end==True:
        answer= -1
    return answer