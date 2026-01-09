ISBN = input()
v=3
sum=0
for i in ISBN:
    if i == '*':
        if v == 1:
            v = 3
        elif v == 3:
            v = 1
        t = v
        continue
    if v==1:
        v=3
    elif v==3:
        v=1
    sum = sum + int(i) * v
    # print("i : ",i," v : ",v)
    # print("sum : ",sum)
for i in range (10):
    if (sum + t * i) % 10 == 0:
        print(i)
        break



