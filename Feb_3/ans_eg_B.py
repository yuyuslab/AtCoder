h, w, n = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

ans = [['.' for _ in range(w)] for _ in range(h)]

x, y, m = 0, 0, 0

for _ in range(n):
    if ans[x][y] == '.':
        ans[x][y] = '#'
        m += 1
    else:
        ans[x][y] = '.'
        m += 3

    m %= 4
    x += dx[m]
    y += dy[m]

    if x < 0:
        x += h
    if x >= h:
        x -= h
    if y < 0:
        y += w
    if y >= w:
        y -= w

for i in range(h):
    print(''.join(ans[i]))




