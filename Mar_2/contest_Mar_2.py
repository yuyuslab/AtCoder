# A, B = map(int, input().split())

# AB = A + B

# lst = list(range(0,10))

# for i in lst:
#     if AB != i:
#         print(i)
#         break

# N = int(input())
# lst = []
# for c in range(N):
#     lst.append(list(map(int, input().split())))

# for i in range(len(lst)):
#     index_lst = []
#     row = lst[i]
#     index = 1
#     for j in row:
#         if j == 1:
#             index_lst.append(index)
#             index += 1
#         else:
#             index += 1
#     print(" ".join(str(x) for x in index_lst))


N = int(input())


for i in range(N):
    N = str(N)
    rev = N[::-1]
    rev = int(rev)
    if rev < int(N):
        if N == rev and rev**(1/3) == int(rev**(1/3)):
            
            break
    else:
        N = int(N) - 1
        print(rev)

