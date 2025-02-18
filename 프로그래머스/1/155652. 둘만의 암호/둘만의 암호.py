def solution(s, skip, index):
    skip_set = set(skip)  # set으로 변환하여 탐색 속도 O(1)로 최적화
    result = []

    for char in s:
        count = 0
        n = ord(char)  # 현재 문자의 아스키 코드 값

        while count < index:
            n = (n + 1 - 97) % 26 + 97  # 'a'~'z' 범위 유지
            if chr(n) not in skip_set:
                count += 1
        
        result.append(chr(n))  # 변환된 문자 추가

    return ''.join(result)  # 리스트를 문자열로 변환 후 반환