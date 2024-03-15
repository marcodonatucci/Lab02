import dictionary


class Translator:

    def __init__(self):
        self.dictionary = dictionary.Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("-----------------------------\n   Translator Alien-Italian   \n-----------------------------\n1. "
              "Aggiungi nuova parola\n2. Cerca una traduzione\n3. Cerca con Wildcard\n4. Stampa tutto il "
              "dizionario\n5. Exit\n------------------------------")

    def loadDictionary(self, string):
        # dict is a string with the filename of the dictionary
        f = open(string, 'r', encoding='UTF-8')
        line = f.readline()
        while len(line) > 0:
            words = line.split(" ")
            word = words[0]
            translation = words[1]
            self.dictionary.addWord(word, translation)
            line = f.readline()
        f.close()

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        entry = entry.lower()
        words = entry.split(" ")
        if len(words) == 2:
            self.dictionary.addWord(words[0], words[1])
            print(f"{words[0]} {words[1]}\nAdded!")
        else:
            for i in range(1,len(words)):
                self.dictionary.addWord(words[0], words[i])
            print(f"{words[0]} {words[1:]}\nAdded!")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query.isalpha():
            query = query.lower()
            translation = self.dictionary.translate(query)
            print(f"{query} -> {translation}")
        else:
            raise ValueError("Alphabetic characters expected")

    def handleWildCard(self, query):
        # query is a string with a ? --> <par?la_aliena>
        results = []
        for key in self.dictionary.words:
            if self.dictionary.translateWordWildCard(query, key):
                results.append(key)
        for word in results:
            print(self.dictionary.words[word])
