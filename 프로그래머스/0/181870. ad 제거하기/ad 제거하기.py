def solution(strArr):
    answer=[]
    for i in range(len(strArr)):
        print(strArr[i])
        print(len(strArr[i]))
        if "ad" not in (strArr[i]) or len(strArr[i])<2:
            print(1)
            answer.append(strArr[i])
    return answer