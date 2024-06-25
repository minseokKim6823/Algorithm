def solution(emergency):
    value1=1
    answer=[0 for i in range(len(emergency))] 
    for i in range(len(emergency)):
        t=emergency.index(max(emergency))
        emergency[t]=-1
        answer[t]=value1
        value1+=1
    return answer