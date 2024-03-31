N, K = map(int, input().split())

A = list(map(int, input().split()))

lst = []

for i in A:
    if i%K == 0:
        lst.append(int(i/K))

lst.sort()

print(*lst)