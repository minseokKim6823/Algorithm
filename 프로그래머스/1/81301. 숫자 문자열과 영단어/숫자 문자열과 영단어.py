def solution(s):
    lst=[]
    lst1=["zero","one","two","three","four","five","six","seven","eight","nine"]
    answer=''
    i=0
    while i<len(s):
        if s[i].isdigit():
            lst.append(int(s[i]))
            i+=1
        else:
            if s[i]=='z':
                lst.append(0)
                i+=4
            elif s[i]=='o':
                lst.append(1)
                i+=3
            elif s[i]=='e':
                lst.append(8)
                i+=5
            elif s[i]=='n':
                lst.append(9)
                i+=4
            elif s[i]=='s':
                if s[i+1]=='e':
                    lst.append(7)
                    i+=5
                elif s[i+1]=='i':
                    lst.append(6)
                    i+=3
            elif s[i]=='t':
                if s[i+1]=='w':
                    lst.append(2)
                    i+=3
                elif s[i+1]=='h':
                    lst.append(3)
                    i+=5
            else:
                if s[i+1]=='o':
                    lst.append(4)
                    i+=4
                else:
                    lst.append(5)
                    i+=4
    for i in range(len(lst)):
        answer+=str(lst[i])
    answer=int(answer)
    return answer