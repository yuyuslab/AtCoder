def INPUT():
    N = int(input())
    S = str(input())
    T =  str(input())
    changeString(N, S, T)

def changeString(N, S, T):
    S_splitted = splitCharacters(S)
    T_splitted = splitCharacters(T)
    S_fixed_and_counter = fixS(N, S_splitted, T_splitted)
    S_fixed = S_fixed_and_counter[0]
    counter = S_fixed_and_counter[1]
    confirmation = confirmSisT(S_fixed, T_splitted, counter)
    print(confirmation)

def splitCharacters(inPut):
    lst = []
    for character in inPut:
        lst.append(character)
    return lst

def fixS(N, S_splitted, T_splitted):
    fixed_S = []
    counter = 1
    for i in range(N):
        if S_splitted[i] is not T_splitted[i]:
            S_splitted[i] = T_splitted[i]
            fixed_S.append(S_splitted[i])
            counter += 1
        else:
            fixed_S.append(S_splitted[i])
    return fixed_S, counter
    
def confirmSisT(fixed_S, T_splitted, counter):
    if fixed_S == T_splitted:
        if counter > 2:
            if counter%2 == 1:
                counter_by_two = counter/2
                count_completed = counter_by_two + 1
                return count_completed
            else:
                counter_by_two = counter/2
                return counter_by_two
        elif counter == 1 or 2:
            return -1
    else:
        print("S was not fixed")

def SIorSJ(S_tobechanged, counter):
    SI = "A"
    SJ = "B"
    if counter%2 == 1:
        replaced = S_tobechanged.replace(S_tobechanged, SI)
        return replaced
    else:
        replaced = S_tobechanged.replace(S_tobechanged, SJ)
        return replaced

def fixS(N, S_splitted, T_splitted):
    fixing_S = []
    counter = 1
    for i in range(N):
        if S_splitted[i] is not T_splitted[i]:
            SIorSJ(S_splitted[i], counter)
            fixing_S.append(S_splitted[i])
            counter += 1
        else:
            fixing_S.append(S_splitted[i])
    return fixing_S, counter



if __name__ == '__main__':
    INPUT()