def compare(word1, word2):
    string1 = ""
    for i, c in enumerate(word2):
        if c in word1:
            if c == word1[i]:
                string1 = string1 + "[ %s ]" % c
            else:
                string1 = string1 + "( %s )" % c
        else:
            string1 = string1 + c

    print(string1)


compare("tiger", "fiest")
