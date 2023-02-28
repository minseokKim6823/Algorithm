list1 = []
for i in range(10):
    n = int(input())
    if (n % 42 in list1) == False:
        list1.append(n % 42)
print(len(list1))
