# N = int(input())

# S = []

# c = 0

# for _ in range(N):
#     S.append(str(input()))

# for i in S:
#     if i == "Takahashi":
#         c += 1
#     else:
#         c = c

# print(c)

N = int(input())

A = list(map(int, input().split()))

c = 0

l = []

while c < len(A) - 2:
    if A[c] + A[c + 2] == A[c]*2:
        l.append(A[c])
        c += 1
    else:
        c += 1

c = 0

while c < len(A) - 3:
    if A[c + 1] + A[c + 3] == A[c + 1]*2:
        l.append(A[c + 1])
        c += 1
    else:
        c += 1

l = set(l)

print(len(l))