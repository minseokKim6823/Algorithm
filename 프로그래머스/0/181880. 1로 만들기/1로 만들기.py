def solution(num_list):
    answer = 0
    for i in range(len(num_list)):
        num=num_list[i]
        if num ==1:
            pass
        else:
            while num!=1:
                if num%2==1:
                    num-=1
                else:
                    num/=2
                    answer+=1        
    return answer