# S, T = map(str, input().split(" "))

# if S == "AtCoder" and T == "Land":
#     print("Yes")
# else:
#     print("No")


N, A = map(int, input().split())

T = list(map(int, input().split()))

i = 0

while i < N:
    Tf = A + T[i]
    if Tf >= T[i + 1]:
        Tf = Tf + A
        i += 1
    elif Tf < T[i]:
        Tf = Tf + T[i + 1] + A
        i += 1
    else:
        print("error")
        exit()

print(Tf)

