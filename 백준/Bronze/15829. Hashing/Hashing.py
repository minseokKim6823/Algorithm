L = int(input())
string = input()
answer = 0

for i in range(L):
    answer += (ord(string[i])-96) * (31 ** i) #아스키 코드 값을 돌려주는 ord함수
print(answer % 1234567891)