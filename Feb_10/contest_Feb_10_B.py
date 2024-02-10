if __name__ == '__main__':

    A = []
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    i = 0
    while i < int(lines[0]):
        query = lines[i+1].split()
        i += 1
        if query[0] == '1':
            A.append(query[1])
        else:
            k = int(query[1])
            print(A[-k])





    Q=int(input())
    A=[]
    for _ in range(Q):
        t,x=map(int,input().split())
    if t==1:
        A.append(x)
    else:
        print(A[-x])

