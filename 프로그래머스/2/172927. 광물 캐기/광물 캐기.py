def solution(picks, minerals):
    answer = 0
    mineralSort = []

    # i)  곡괭이보다 광석이 많을 때
    # ii) 광석보다 곡괭이가 많을 때
    ableDigAmount = min(sum(picks) * 5, len(minerals))
    diaCnt, ironCnt, stoneCnt = 0, 0, 0

    for i in range(ableDigAmount):
        if minerals[i] == 'diamond':
            diaCnt += 1
        elif minerals[i] == 'iron':
            ironCnt += 1
        elif minerals[i] == 'stone':
            stoneCnt += 1
        
        # 5개씩 튜플로 만들어 리스트에 추가
        # 5단위로 끊기지 않으면 마지막 그룹은 i = ableDigAmout - 1일 때 에 튜플로 추가
        if (i + 1) % 5 == 0 or i == ableDigAmount - 1:
            mineralSort.append((diaCnt, ironCnt, stoneCnt))
            diaCnt, ironCnt, stoneCnt = 0, 0, 0

    # 좋은 광물이 많을 수록 앞에 위치하도록 정렬
    mineralSort.sort(key = lambda x : (x[0], x[1], x[2]), reverse = True)

    # 좋은 곡괭이를 먼저 사용
    i = 0
    for diaCnt, ironCnt, stoneCnt in mineralSort:
        # 해당 등급 곡괭이가 없으면 다음등급 곡괭이
        while picks[i] == 0:
            i += 1

        # 피로도 계산
        if i == 0:
            answer += (diaCnt + ironCnt + stoneCnt)
        elif i == 1:
            answer += (diaCnt * 5 + ironCnt + stoneCnt)
        elif i == 2:
            answer += (diaCnt * 25 + ironCnt * 5 + stoneCnt)

        # 곡괭이를 사용했으니 파괴
        picks[i] -= 1

    return answer