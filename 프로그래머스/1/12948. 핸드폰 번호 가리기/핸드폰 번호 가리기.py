def solution(phone_number):
    cnt=len(phone_number)-4
    lst1=['*']*cnt
    for i in range(cnt,len(phone_number)):
        lst1.append(phone_number[i])
    answer= ''.join(lst1)
    return answer