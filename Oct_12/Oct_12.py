# N = int(input())
# S = str(input())


# subS = S[0:-2]

# i = 0
# c = 0


# while i < N-2:
#     if subS[i] == "#" and S[i+2] == "#" and S[i+1] == ".":
#         c += 1
#         i += 1
#     else:
#         c = c
#         i += 1

# print(c)


# N = int(input())

# l = []

# cost = 0

# for _ in range(N):
#     l.append(list(map(int, input().split())))

# for i in range(N-1):
#     x_cost = (l[i+1][0] - l[i][0])**2
#     y_cost = (l[i+1][1] - l[i][1])**2

#     sub_cost = (x_cost + y_cost)**0.5
#     cost += sub_cost

# return_cost =  ((l[-1][0])**2 + (l[-1][1])**2)**0.5

# zero_move_cost =  ((l[0][0])**2 + (l[0][1])**2)**0.5

# cost = zero_move_cost + cost + return_cost

# print(cost)


# N = int(input())

# l = []


# for _ in range(N):
#     sub_l = []
#     row = str(input())
#     for s in row:
#         sub_l.append(s)
#     l.append(sub_l)

# print(l)


