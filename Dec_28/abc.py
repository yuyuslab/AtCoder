A, B, C, D = map(int, input().split())

if A == B:
    if C == D:
        print("Yes1")
    else:
        print("No2")
elif B == C:
    if A == D:
        print("Yes3")
    else:
        print("No4")
else:
    print("No5")


