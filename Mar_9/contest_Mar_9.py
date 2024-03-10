# S = str(input())
# lst = []
# ct = 0
# for i in S:
#     if i == "|":
#         lst.append(ct)
#         ct += 1
#     else:
#         ct += 1


# before = S[:lst[0]]
# after = S[lst[1]+1:]

# print(before + after)
# lst = []

# while True:
#     A = int(input())
#     lst.append(A)
#     if A == 0:
#         break

# for i in lst[::-1]:
#     print(i)

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

L = int(input())
C = list(map(int, input().split()))

X = int(input())
Q = list(map(int, input().split()))

sumlst = []


for i in A:
    for j in B:
        for k in C:
            s = i + j + k
            sumlst.append(s)

for q in Q:
    if q in sumlst:
        print("Yes")
    else:
        print("No")

        
'''
#This takes toooo long

for q in Q:
    if min(sumlst) <= q <= max(sumlst):
        for m in sumlst:
            if q == m:
                print("Yes")
    else:
        print("No")

'''


