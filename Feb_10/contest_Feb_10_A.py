if __name__ == '__main__':
    a, b, d = map(int, input().split())

    lst = []
    additive = 0

    if a + d > b:
        print(a)
    else:
        while a + additive <= b:
            lst.append(a + additive)
            additive += d
        for i in lst:
            print(i, end='\r')



