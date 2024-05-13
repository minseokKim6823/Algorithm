while True:
    lst = []
    S=input()
    if S==".":
        break
    elif S[0] == ')':
        print('no')
        continue
    elif S[0] == ']':
        print('no')
        continue
    elif S[0] == '(' or S[0] == '[':
        lst.append(S[0])
        for i in range(1,len(S)):
            if S[i]=='(' or S[i]=='[':
                lst.append(S[i])
            elif S[i]==')':
                if len(lst)>=1 and lst[len(lst)-1]=='(':
                    lst.pop()
                else:
                    lst.append(S[i])
            elif S[i] == ']':
                if len(lst)>=1 and lst[len(lst)-1]=='[':
                    lst.pop()
                else:
                    lst.append(S[i])
            else:
                pass
    else:
        for i in range(1, len(S)):
            if S[i] == '(' or S[i] == '[':
                lst.append(S[i])
            elif S[i] == ')':
                if len(lst)>=1 and lst[len(lst) - 1] == '(':
                    lst.pop()
                else:
                    lst.append(S[i])
            elif S[i] == ']':
                if len(lst)>=1 and lst[len(lst) - 1] == '[':
                    lst.pop()
                else:
                    lst.append(S[i])
            else:
                pass

    if len(lst)==0:
        print("yes")
    else:
        print("no")