a=-1
while a!=0:
    result = "wrong"
    a,b,c = map(int,input().split())
    if a==0:
        break
    max=a
    if b>max:
        max=b
    if c>max:
        max=c
    if max**2==a**2+c**2+b**2-max**2:
        result="right"
    print(result)