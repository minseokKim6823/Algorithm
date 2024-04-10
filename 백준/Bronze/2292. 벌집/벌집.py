input_value=1
value=0
N=int(input())
lst=[]
if N==1:
    print(1)
else:
    while N > input_value:
        lst.append(input_value + value * 6)
        input_value = input_value + value * 6
        value += 1
    for i in range(len(lst)):
        if lst[i] >= N:
            print(i + 1)

