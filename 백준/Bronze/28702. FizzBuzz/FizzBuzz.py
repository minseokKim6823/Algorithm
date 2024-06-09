lst1=[]
d=3
result=0
for i in range(3):
    T=input()
    if T=="Fizz" or T=="Buzz" or T=="FizzBuzz":
        pass
    else:
        T=int(T)
        result=int(T)+d
        lst1.append(result)
        break
    d-=1
if result%3==0 and result%5==0:
    print("FizzBuzz")
elif result%5==0:
    print("Buzz")
elif result%3==0:
    print("Fizz")
else:
    print(result)