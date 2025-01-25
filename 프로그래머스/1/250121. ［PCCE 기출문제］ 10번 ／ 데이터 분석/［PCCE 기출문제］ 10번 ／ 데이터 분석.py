def solution(data, ext, val_ext, sort_by):
    answer = []
    value1=0
    value2=0
    if ext=="date":
        value1=1
    elif ext=="maximum":
        value1=2
    elif ext=="remain":
        value1=3
        
    if sort_by=="date":
        value2=1
    elif sort_by=="maximum":
        value2=2
    elif sort_by=="remain":
        value2=3
    data.sort(key=lambda x:x[value2])
    for i in range(len(data)):
        if data[i][value1]<=val_ext:
            answer.append(data[i])
    if len(answer)==0:
        answer=[[]]
    return answer