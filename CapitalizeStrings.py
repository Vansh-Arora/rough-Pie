def to_jaden_case(string):
    wordArray = string.split()
    wordArray2 = []
    for word in wordArray:
        wordArray2.append(word.capitalize())
    space = " "
    return (space.join(wordArray2))

to_jaden_case("i ma groot")