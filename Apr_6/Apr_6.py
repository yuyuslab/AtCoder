# N = int(input())

# i = 1

# lst = []

# while i < N + 1:
#     if i%3 == 0:
#         lst.append("x")
#     else:
#         lst.append("o")
#     i += 1

# print("".join(lst))

import math

N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

i = 0
c = 1

lst = []

while i < N:
    
    xi = l[i][0]
    yi = l[i][1]
    i += 1

    while c < N:
        xc = l[c][0]
        yc = l[c][1]
        c += 1
        doubled = (xi - xc)**2 + (yi - yc)**2
        # print(doubled)
        d = math.sqrt(doubled)
        lst.append(d)
    m = max(lst)
    print(lst)
    ind = lst.index(m)
    # print(ind + 1)

    





















