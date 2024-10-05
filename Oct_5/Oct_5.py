# S = str(input())

# sanOrnot = S[-3:]

# if sanOrnot == 'san':
#   print("Yes")
# else:
#   print("No")




# S = str(input())
# T = str(input())

# i = 0

# if S == T:
#     print(i)
#     exit()
# elif len(S) == len(T):
#     while i < len(S):
#         if S[i] == T[i]:
#             i += 1
#         else:
#             i += 1
#             print(i)
#             exit()
# elif len(S) > len(T):
#     while i < len(T):
#       if S[i] == T[i]:
#           i += 1
#       else:
#           i += 1
#           print(i)
#           exit()
#     print(len(T) + 1)
#     exit()
# else:
#     while i < len(S):
#       if S[i] == T[i]:
#           i += 1
#       else:
#           i += 1
#           print(i)
#           exit()
#     print(len(S) + 1)
#     exit()


# 以下は違うっぽい       
# N = int(input())

# K = list(map(int, input().split()))

# A = []

# B = []

# i = 1
# K.sort()
# length = len(K) + 1

# while i < len(K) + 1:
#     if sum(A) < sum(B):
#         A.append(K[-i])
#         i += 1
#     else:
#         B.append(K[-i])
#         i += 1

# print(max(sum(A), sum(B)))


N = input()

K = list(map(int, input().split()))

binary = len(K) << 1

print(binary)

