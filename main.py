import translator as tr

t = tr.Translator()


while True:

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        txtInp = input("Write the word and the translation separated by an empty space: ")
        t.handleAdd(txtInp)
    if int(txtIn) == 2:
        txtInp = input("Write the word to translate: ")
        t.handleTranslate(txtInp)
    if int(txtIn) == 3:
        txtInp = input("Write the word to translate with a wildcard '?': ")
        t.handleWildCard(txtInp)
    if int(txtIn) == 4:
        print(t.dictionary.words)
    if int(txtIn) == 5:
        exit()
