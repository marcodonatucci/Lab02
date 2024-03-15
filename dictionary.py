class Dictionary:
    def __init__(self):
        self.words = {}

    def addWord(self, word, translation):
        if word in self.words:
            self.words[word].append(translation)
        else:
            self.words[word] = [translation]

    def translate(self, word):
        return self.words[word]

    def translateWordWildCard(self, word, key):
        if len(word) != len(key):
            return False
        for char1, char2 in zip(word, key):
            if char1 != char2 and char1 != '?':
                return False
        return True


