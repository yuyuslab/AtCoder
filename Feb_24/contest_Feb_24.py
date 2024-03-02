# S = str(input())
# s_split = [i for i in S]

# s = 0
# while s < len(S) + 1:
#     if s < len(S):
#         if S[s] != S[s+1]:
#             if s == 0 and S[s] != S[2]:
#                 print(s+1)
#                 break
#             else:
#                 print(s+2)
#                 break
#         else:
#             s += 1
#     else:
#         print(s)
#         break


# N = int(input())
# P = list(map(int, input().split()))
# Q = int(input())
# lst = []
# i = 0
# while i < Q:
#     A, B = map(int, input().split())
#     if P.index(A) < P.index(B):
#         lst.append(A)
#     else:
#         lst.append(B)
#     i += 1

# for s in lst:
#     print(s)

N = int(input())
S = str(input())
ss = [i for i in S]
Q = int(input())
i = 0

while i < Q:
    c, d = map(str, input().split())
    for s in ss:
        if s == c:
            ss[i] = d
        else:
            ss[i] = ss[i]
    i += 1

print(ss)
