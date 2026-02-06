N = int(input())
dice = list(map(int,input().split(' ')))
square = N*N*5
answer = 0

if N == 1 :
    dice.sort()
    print(sum(dice[:5]))
else :
    answer = 0
    pair = []
    for i in range(3):
        pair.append(min(dice[i],dice[-1-i]))
    pair.sort()

    answer += 4*sum(pair)
    square -= 4*3

    answer += (8*N-12)*sum(pair[:2])
    square -= (8*N-12)*2
    
    answer += square*pair[0]
    print(answer)