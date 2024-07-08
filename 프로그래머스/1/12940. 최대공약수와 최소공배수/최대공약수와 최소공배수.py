def solution(n, m):
    answer = []
    result=n*m
    while m>0:
        n,m=m,n%m
    answer.append(n)
    answer.append(result//n)
    return answer