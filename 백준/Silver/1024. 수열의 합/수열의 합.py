N, L = map(int, input().split())
for i in range(L, 101):
    s = i * (i - 1) // 2  # 이것도 공식으로 바꾸면 더 깔끔
    if s > N:
        print(-1)
        break
    if (N - s) % i == 0 and (N - s) // i >= 0:
        start = (N - s) // i
        print(' '.join(map(str, range(start, start + i))))
        break
else:  # for문이 break 없이 끝났을 때
    print(-1)