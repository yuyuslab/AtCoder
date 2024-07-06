# Question A
# N, K, X = map(int, input().split())

# A = list(map(int, input().split()))

# leng = len(A)

# A1 = A[0:K:]
# A2 = A[K:leng:]

# A1.append(X)

# A = A1 + A2

# print(*A)



# Question B
# a, b, c, d, e, f = map(int, input().split())
# g, h, i, j, k, l = map(int, input().split())

# x, y, z = 0, 0, 0


# if j <= a or d <= g:
#   x = x + 1

# if k <= b or e <= h:
#   y = y + 1

# if l <= c or f <= i:
#   z = z + 1

# if x + y + z == 0:
#   print("Yes")
# else:
#   print("No")

# Question C
# N, K = map(int, input().split())

# A = list(map(int, input().split()))

# A.sort()


# r = N - K - 1

# c = 0

# pd = 10^9

# while r + c <= N:
#     cd = A[r + c] - A[c]
#     if cd < pd:
#         pd = cd
#     c += 1

# print(pd)





