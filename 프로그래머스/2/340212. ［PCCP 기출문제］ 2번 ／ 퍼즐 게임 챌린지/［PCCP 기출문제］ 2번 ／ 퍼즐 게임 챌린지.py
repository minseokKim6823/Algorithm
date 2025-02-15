def solution(diffs, times, limit):
    max_level = max(diffs)  #최대 diff 구해두기
    l = 1
    r = max_level
    answer = max_level
    while l < r:
        level = int((l + r) /2)
        time = times[0]
        
        for i in range(1, len(diffs)):
            k = 0
            if level < diffs[i]:
                k = diffs[i] - level
            time += (times[i] + times[i -1]) * k + times[i]
            
        if time <= limit:
            r = level
            answer = level  
            
        else:
            l = level +1  
        

    return answer
