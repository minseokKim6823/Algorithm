def solution(my_string, s, e):
    answer = ''
    lst1=[]
    for i in range(s):
        lst1.append(my_string[i])
    for i in range(e,s-1,-1):
        lst1.append(my_string[i])
    for i in range(e+1,len(my_string)):
        lst1.append(my_string[i])
    answer=answer.join(''.join(lst1))
    return answer