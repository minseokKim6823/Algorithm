lst=[]
result="Scalene"
for i in range(3):
    angle=int(input())
    if angle!=60 and angle in lst:
        lst.append(angle)
        result = "Isosceles"
    elif angle ==60 and angle in lst:
        lst.append(angle)
        result = "Equilateral"
    else:
        lst.append(angle)
if sum(lst)!=180:
    result = "Error"
print(result)
