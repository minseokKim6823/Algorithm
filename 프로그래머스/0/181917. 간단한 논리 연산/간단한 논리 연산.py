def solution(x1, x2, x3, x4):
    answer=[]
    if x1==True:
        answer.append(1)
    elif x2==True:
        answer.append(1)
    else:
        answer.append(0)
    if x3==True:
        answer.append(1)
    elif x4==True:
        answer.append(1)
    else:
        answer.append(0)
    if 0 not in answer:
        result=True
    else:
        result=False
    return result