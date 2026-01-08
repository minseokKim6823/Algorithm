room = input()
lst = [0 for i in range(10)]
for i in range(len(room)):
    if room[i] == '6':
        lst[9] += 1
    elif room[i] == '9':
        lst[6] += 1
    lst[int(room[i])]+=1
if int(lst[9]) % 2 != 0 :
    lst[9] = lst[9]// 2 + 1
    lst[6] = lst[6]// 2 + 1
else:
    lst[9] = lst[9]// 2
    lst[6] = lst[6]// 2
print(max(lst))