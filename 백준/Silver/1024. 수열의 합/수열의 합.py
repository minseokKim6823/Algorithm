N, L = map(int, input().split())

found = False
for i in range(L, 101):
    base_sum = i * (i - 1) // 2
    
    if base_sum > N:
        break
    
    if (N - base_sum) % i == 0:
        start = (N - base_sum) // i
        if start >= 0:  # 시작값이 음수면 안됨
            print(' '.join(map(str, range(start, start + i))))
            found = True
            break

if not found:
    print(-1)