def solution(keymap, targets):
    dic={}
    # dic[0]=0
    # dic[1]=1
    # dic[2]=2
    # dic[3]=3
    # dic[4]=4
    # print(dic[1])
    # print(dic)
    answer = []
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in dic:
                dic[keymap[i][j]]=j+1
            if keymap[i][j] in dic:
                if dic[keymap[i][j]]>j:
                    dic[keymap[i][j]] = j+1
    for i in range(len(targets)):
        v=0
        for j in range(len(targets[i])):
            if targets[i][j] not in dic:
                v=-1
                break
            else:
                v+= dic[targets[i][j]]
        answer.append(v) 
    return answer