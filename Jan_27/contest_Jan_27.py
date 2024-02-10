# Problem A
def INPUT():
    INPUT = str(input())
    splitted_letters = splitCharacters(INPUT)
    checked_letters = letterCheck(splitted_letters)
    firstUPorNot(checked_letters)


def splitCharacters(INPUT):
    splitted_letters = []
    for letter in INPUT:
        splitted_letters.append(letter)
    return splitted_letters

def letterCheck(splitted_letters):
    torf = []
    for checked_letter in splitted_letters:
        if checked_letter.isupper() == True:
            torf.append("upper")
        else:
            torf.append("lower")
    return torf


def firstUPorNot(torf):
    fist_letter = torf[0]
    lst = torf
    if fist_letter == "upper":
        whileLoop(lst)
    else:
        print("No")

def whileLoop(torf):
    judge = "Yes"
    for other_letter in torf[1:len(torf)]:
        if other_letter == "lower":
            judge = "Yes"
        elif other_letter == "upper":
            judge = "No"
            break
    print(judge)



if __name__ == '__main__':
    INPUT()