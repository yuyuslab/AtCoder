S = str(input())

s = S.replace('ABC', '')


lst = []

i = 1

while i < 350:
    stri = str(i).zfill(3)
    lst.append(stri)
    i += 1

del lst[315]
    
if s in lst:
    print('Yes')
else:
    print('No')
