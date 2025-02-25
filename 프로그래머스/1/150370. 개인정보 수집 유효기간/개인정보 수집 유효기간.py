def solution(today, terms, privacies):
    dict={}
    answer = []
    t_year=int(today[0])*1000+int(today[1])*100+int(today[2])*10+int(today[3])
    t_month=int(today[5])*10+int(today[6])
    t_day=int(today[8])*10+int(today[9])
    dict = {item.split()[0]: int(item.split()[1]) for item in terms}
    for i in range(len(privacies)):
        year=int(privacies[i][0])*1000+int(privacies[i][1])*100+int(privacies[i][2])*10+int(privacies[i][3])
        month=int(privacies[i][5])*10+int(privacies[i][6])
        day=int(privacies[i][8])*10+int(privacies[i][9])
        check=privacies[i][11]
        month+=dict[check]
        if month > 12:
            year += month // 12
            month = month % 12
            if month == 0:
                month = 12
                year -= 1
        if t_year>year:
            answer.append(i+1)
        elif t_year==year:
            if t_month>month:
                answer.append(i+1)
            elif t_month==month:
                if t_day>=day:
                    answer.append(i+1)
    return answer