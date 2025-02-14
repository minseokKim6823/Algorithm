def solution(n, q, ans):
    answer = 0
    for a in range(1,n-3):
        for b in range(a+1,n-2):
            for c in range(b+1,n-1):
                for d in range(c+1,n):
                    for e in range(d+1,n+1):
                        list1=[]
                        list1.append(a)
                        list1.append(b)
                        list1.append(c)
                        list1.append(d)
                        list1.append(e)
                        result2=0
                        for i in range(len(q)):
                            result1=0
                            t=ans[i]
                            for j in range(len(list1)):
                                if list1[j] in q[i]:
                                    result1+=1
                            if result1==t:
                                result2+=1
                        if result2==len(ans):
                            answer +=1
    return answer