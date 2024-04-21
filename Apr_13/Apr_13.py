# N = int(input())

# A = list(map(int, input().split()))

# sum = sum(A[0:N-1])

# print(sum * -1)

S = [*str(input())]

alp = list(set(S))

lst = []

for i in alp:
    cnt = 0
    t = 0
    while t < len(S):
        if i in S:
            cnt += 1
            t += 1
        else:
            t += 1
    lst.append(cnt)

print(lst)
