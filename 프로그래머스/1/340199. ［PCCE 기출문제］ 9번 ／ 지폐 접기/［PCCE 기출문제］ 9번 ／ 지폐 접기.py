def solution(wallet, bill):
    answer = 0
    while min(wallet)<min(bill) or max(wallet)<max(bill):
            if bill[0]>bill[1]:
                bill[0]//=2
            else:
                bill[1]//=2
            answer+=1
    return answer