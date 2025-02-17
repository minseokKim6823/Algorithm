def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    best_range = None  # 최소 길이 구간 저장

    while right < len(sequence):
        if current_sum == k:
            if best_range is None or (right - left < best_range[1] - best_range[0]):
                best_range = [left, right]

        if current_sum < k:
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            current_sum -= sequence[left]
            left += 1

    # 단일 원소로 `k`가 존재하는 경우, 최소 길이를 고려하여 처리
    if k in sequence:
        index = sequence.index(k)
        single_range = [index, index]
        if best_range is None or (single_range[1] - single_range[0] < best_range[1] - best_range[0]):
            return single_range

    return best_range if best_range else []
