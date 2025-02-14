def solution(name, yearning, photo):
    answer = []
    dict={}
    for i in range(len(name)):
            dict[name[i]]=yearning[i]
    for i in range(len(photo)):
        value=0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                value+=dict[photo[i][j]]
        answer.append(value)
    return answer