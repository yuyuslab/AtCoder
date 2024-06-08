# N, M = map(int, input().split())
# hands = list(map(int, input().split()))

# i = 0

# while i < N:
#     M = M - hands[i]
#     if M >= 0:
#         i += 1
#     else:
#         break

# print(i)

# S = str(input())
# c = 0
# for i in S:
#     if i.isupper():
#         c += 1
#     else:
#         c = c

# if c > len(S)/2:
#     print(S.upper())
# else:
#     print(S.lower())


# N = int(input())

# grid = list([['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]*(3**N))

# i = 0
# while i < 3**N:
#     print(grid[i - 2])
#     print(grid[i - 1])
#     print(grid[i], end="\n")
#     i += 3
# んーーーー
