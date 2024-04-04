n=int(input())
cnt1=0
cnt2=0
def fib(n):
    global cnt1
    if (n == 1 or n == 2):
        cnt1+=1
        return 1  # 코드1
    else:
        cnt1 += 1
        return (fib(n - 1) + fib(n - 2))
def fibonacci(n):
    return n-2
fib(n)
cnt2=fibonacci(n)
print((cnt1+1)//2,cnt2)


