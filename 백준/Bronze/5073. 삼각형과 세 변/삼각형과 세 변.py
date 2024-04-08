while 1:
    a, b, c = map(int, input().split())
    if a == 0:
        break
    max1 = max(a,b,c)
    if a + b + c - max1 <= max1:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    elif a != b != c:
        print("Scalene")