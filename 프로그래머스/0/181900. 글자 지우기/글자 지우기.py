def solution(my_string, indices):
    lst1=[]
    for i in range(len(my_string)):
        if i not in indices:
            lst1.append(my_string[i])
    answer = ''.join(lst1)
    return answer