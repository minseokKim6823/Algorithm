def solution(my_string):
    lst1=[]
    for i in range(len(my_string)):
        if my_string[i] not in lst1:
            lst1.append(my_string[i])
    answer=''.join(lst1)
    return answer