H,M=map(int,input().split())
if M<45:
    if(H==0):
        H=23
        L = 45 - M
        M = 60 - L
    else:
        H -= 1
        L = 45 - M
        M = 60 - L
elif M>=45:
    M -=45
print(H,M)