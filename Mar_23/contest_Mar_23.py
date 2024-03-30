# N = int(input())

# A = list(map(int, input().split()))

# lst = []
# i = 0
# while i < N:
#     if i != N - 1:
#         b = A[i]*A[i + 1]
#         lst.append(b)
#         i += 1
#     else:
#         break


# print(*lst)

##################

# W, B = map(int, input().split())

# if B == 0:
#     if W == 0: print("Yes")
#     else: print("No")
# elif B%2 == 0: 
#     if W%2 == 0 or W%3 == 0: print("Yes")
#     else: print("No")
# elif B%3 == 0: 
#     if W%4 == 0 or W%3 == 0: print("Yes")
#     else: print("No")
# elif B%5 == 0:
#     if W%6 == 0: print("Yes")
#     else: print("No")
# else:
#     print("No")

###########

N, K = map(int, input().split())

A = map(int, input().split())
sA = set(A)

lst = []
i = 1

while i <= K:
    if i not in sA:
        lst.append(i)
        i += 1
    else:
        i += 1

print(sum(lst))









