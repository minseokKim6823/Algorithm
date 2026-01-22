king, stone, n = input().split()
n = int(n)

# 방향 정의
move = {
    "R":  (1, 0),
    "L":  (-1, 0),
    "B":  (0, -1),
    "T":  (0, 1),
    "RT": (1, 1),
    "LT": (-1, 1),
    "RB": (1, -1),
    "LB": (-1, -1)
}

# 체스 좌표 → 숫자
kx, ky = ord(king[0]) - ord('A'), int(king[1]) - 1
sx, sy = ord(stone[0]) - ord('A'), int(stone[1]) - 1

for _ in range(n):
    cmd = input()
    dx, dy = move[cmd]

    nkx, nky = kx + dx, ky + dy

    # 킹이 체스판 밖이면 무시
    if not (0 <= nkx < 8 and 0 <= nky < 8):
        continue

    # 돌과 겹칠 경우
    if nkx == sx and nky == sy:
        nsx, nsy = sx + dx, sy + dy
        # 돌이 밖으로 나가면 무시
        if not (0 <= nsx < 8 and 0 <= nsy < 8):
            continue
        sx, sy = nsx, nsy

    kx, ky = nkx, nky

# 숫자 → 체스 좌표
print(chr(kx + ord('A')) + str(ky + 1))
print(chr(sx + ord('A')) + str(sy + 1))
